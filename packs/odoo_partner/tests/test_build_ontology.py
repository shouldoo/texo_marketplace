"""Parser tests for packs/odoo_partner/scripts/build_ontology.py (no database). Run from the repository root:
    python3 -m unittest discover -s packs/odoo_partner/tests
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_ontology as ou  # noqa: E402

ANALYSIS = """---Models in module 'uom'---
obsolete model uom.category
---Fields in module 'purchase'---
purchase     / purchase.order.line      / product_uom (many2one)        : DEL relation: uom.uom
purchase     / purchase.order.line      / product_uom_id (many2one)     : NEW relation: uom.uom

# DONE: renamed in pre-migration

purchase     / purchase.order           / state (selection)             : selection_keys removed: [done]

# DONE: mapped done to purchase

---XML records in module 'uom'---
DEL uom.category: uom.product_uom_categ_kgm
DEL res.country: base.zz
DEL ir.ui.view: purchase.purchase_order_view_tree
"""

PRE_MIGRATION = """
renamed_fields = [
    ("purchase.order.line", "purchase_order_line", "product_uom", "product_uom_id"),
    ("purchase.order", "purchase_order", "notes", "note"),
]
added_fields = [("locked", "purchase.order", "purchase_order", "boolean", None, "purchase", False)]
"""

APRIORI = """
renamed_modules = {"pos_viva_wallet": "pos_viva_com"}
merged_models = {"old.model": "new.model"}
other = {"ignored": "yes"}
"""


class AnalysisTest(unittest.TestCase):
    def setUp(self):
        self.changes = ou.parse_analysis(ANALYSIS, "19.0", "ref")

    def find(self, kind, name):
        return [c for c in self.changes if c.kind == kind and c.name == name]

    def test_field_removed_and_added_with_note(self):
        removed, = self.find("field", "product_uom")
        added, = self.find("field", "product_uom_id")
        self.assertEqual((removed.change, removed.model, removed.field_type), ("removed", "purchase.order.line", "many2one"))
        self.assertEqual(added.change, "added")
        self.assertEqual(removed.note, "DONE: renamed in pre-migration")

    def test_comment_does_not_leak_to_next_group(self):
        state, = self.find("field", "state")
        self.assertEqual(state.note, "DONE: mapped done to purchase")

    def test_selection_key_removed(self):
        sel, = self.find("selection", "state:done")
        self.assertEqual((sel.change, sel.model), ("removed", "purchase.order"))

    def test_obsolete_model_and_versions(self):
        model, = self.find("model", "uom.category")
        self.assertEqual((model.change, model.from_version, model.to_version), ("removed", "18.0", "19.0"))

    def test_xmlid_filter_keeps_views_and_records_of_removed_models(self):
        removed_models = {"uom.category"}
        kept = {c.name for c in self.changes if c.kind == "xmlid" and ou.keep_xmlid(c, removed_models)}
        self.assertEqual(kept, {"uom.product_uom_categ_kgm", "purchase.purchase_order_view_tree"})


class PreMigrationTest(unittest.TestCase):
    def test_renamed_fields_tuples_only(self):
        changes = ou.parse_pre_migration(PRE_MIGRATION, "purchase", "19.0", "ref")
        self.assertEqual([(c.model, c.name, c.new_name) for c in changes],
                         [("purchase.order.line", "product_uom", "product_uom_id"), ("purchase.order", "notes", "note")])
        self.assertTrue(all(c.change == "renamed" and c.source == "openupgrade:pre-migration" for c in changes))

    def test_syntax_error_is_ignored(self):
        self.assertEqual(ou.parse_pre_migration("def (", "m", "19.0", "ref"), [])


class AprioriTest(unittest.TestCase):
    def test_known_dicts_only(self):
        changes = ou.parse_apriori(APRIORI, "19.0", "ref")
        self.assertEqual({(c.kind, c.change, c.name, c.new_name) for c in changes},
                         {("module", "renamed", "pos_viva_wallet", "pos_viva_com"),
                          ("model", "merged", "old.model", "new.model")})



class RenderTest(unittest.TestCase):
    def test_markdown_groups_dedupes_and_summarises_records_of_removed_models(self):
        C = ou.Change
        changes = [
            C("17.0", "model", "account.tax.template", "removed", module="account", model="account.tax.template"),
            C("17.0", "field", "partner_id", "renamed", module="sale", model="sale.order", new_name="customer_id"),
            C("17.0", "field", "partner_id", "renamed", module="sale", model="sale.order", new_name="customer_id"),
            C("17.0", "xmlid", "l10n_it.tax_1", "removed", module="l10n_it", model="account.tax.template"),
            C("17.0", "xmlid", "l10n_it.tax_2", "removed", module="l10n_it", model="account.tax.template"),
            C("17.0", "xmlid", "l10n_it.view_x", "removed", module="l10n_it", model="ir.ui.view"),
        ]
        md = ou.render("17.0", changes, "OpenUpgrade@abc")
        self.assertIn("# Cambi da Odoo 16.0 a 17.0", md)
        self.assertTrue(md.startswith('---\ntype: "Ontology"\ntitle: "Cambi da Odoo 16.0 a 17.0 (Community)"\n'))
        self.assertEqual(md.count("`sale.order.partner_id`: renamed → `customer_id`"), 1)
        self.assertIn("- 2 record di `account.tax.template` rimossi insieme al modello", md)
        self.assertIn("`l10n_it.view_x`: removed", md)
        self.assertNotIn("tax_1", md)


if __name__ == "__main__":
    unittest.main()
