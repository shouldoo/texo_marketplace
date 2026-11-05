"""The demo data of the pack without an Odoo: fictional, consistent with the loader of the core and with the
question set. The core is the folder named by TEXO_CORE, or the checkout CI puts in .core/.

    TEXO_CORE=<core> python3 -m unittest discover -s packs/odoo_partner/tests
"""
import json
import os
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE_SCRIPTS = Path(os.environ.get("TEXO_CORE") or ROOT.parents[1] / ".core") / "scripts"
sys.path.insert(0, str(ROOT / "demo"))
sys.path.insert(0, str(CORE_SCRIPTS))
import data  # noqa: E402
import load_demo  # noqa: E402

ACTIVITIES = {"analysis", "communication", "code", "deploy", "data", "migration"}
SECTIONS = {"profile", "operations", "compliance", "sector", "offer"}


def anchored():
    """(where, item) of every rule, document and note of the organisation's projects and of the customers."""
    for customer in data.CUSTOMERS:
        for key in ("rules", "documents", "notes"):
            for item in customer[key]:
                yield customer, item


class DemoDataTest(unittest.TestCase):

    def test_the_loader_reads_this_data(self):
        self.assertTrue(hasattr(load_demo, "seed"))
        for name in ("DATABASES", "TOKEN_NAME", "TOKEN_DAYS", "COMPANY", "USERS", "WORK_GROUPS", "TEAM",
                     "DELIVERY_STAGES", "TICKET_STAGES", "HOME_STAGES", "TICKET_TAG", "ASSISTANCE",
                     "SOURCES_FOLDER", "ATTACHMENTS", "ORGANISATION", "CUSTOMERS", "LESSONS", "EVAL"):
            self.assertTrue(hasattr(data, name), name)

    def test_only_demo_databases_and_fictional_people(self):
        self.assertTrue(all(db.startswith("demo-") for db in data.DATABASES))
        logins = [login for _, login, _ in data.USERS.values() if login]
        self.assertTrue(all(login.endswith(".example") for login in logins))
        self.assertTrue(data.COMPANY["email"].endswith(".example"))
        self.assertTrue(set(data.TEAM) <= set(data.USERS))
        self.assertEqual(data.USERS["admin"][1], None, "the admin is base.user_admin")

    def test_activities_and_sections_exist_in_hub_and_pack(self):
        rules = list(data.ORGANISATION["rules"]) + [item for _, item in anchored() if "severity" in item]
        for rule in rules:
            self.assertTrue(set(rule.get("activities") or []) <= ACTIVITIES, rule["name"])
            self.assertIn(rule["severity"], ("never", "must", "prefer"))
        notes = list(data.ORGANISATION["notes"]) + [i for _, i in anchored() if i.get("kind")]
        for item in rules + notes:
            if item.get("section"):
                self.assertIn(item["section"], SECTIONS, item["name"])
        for lesson in data.LESSONS:
            self.assertTrue(set(lesson.get("activities") or []) <= ACTIVITIES, lesson["key"])

    def test_every_anchor_resolves(self):
        documents = {d["key"] for d in data.ORGANISATION["documents"]}
        documents |= {d["key"] for c in data.CUSTOMERS for d in c["documents"]}
        for customer, item in anchored():
            where = item["where"]
            projects = {p["name"]: p for p in customer["projects"]}
            if where in ("customer", "organisation"):
                continue
            kind, _, name = where.partition(":")
            if kind == "project":
                self.assertIn(name, projects, where)
            else:
                self.assertEqual(kind, "task", where)
                project, _, task = name.partition("/")
                self.assertIn(task, [t["name"] for t in projects[project]["tasks"]], where)
            if item.get("document"):
                self.assertIn(item["document"], documents)
        for item in data.ORGANISATION["rules"] + data.ORGANISATION["notes"]:
            if item.get("document"):
                self.assertIn(item["document"], documents)
        for document in data.ORGANISATION["documents"] + [d for c in data.CUSTOMERS for d in c["documents"]]:
            if document.get("text_file"):
                self.assertTrue((ROOT / "demo" / "texts" / f"{document['text_file']}.md").is_file())

    def test_tasks_milestones_parents_and_stages(self):
        for customer in data.CUSTOMERS:
            for project in customer["projects"]:
                milestones = {m[0] for m in project["milestones"]}
                names = []
                for task in project["tasks"]:
                    self.assertIn(task["stage"], data.DELIVERY_STAGES)
                    self.assertIn(task["who"], data.USERS)
                    if task.get("milestone"):
                        self.assertIn(task["milestone"], milestones)
                    if task.get("parent"):
                        self.assertIn(task["parent"], names, "a parent comes before its subtask")
                    if task.get("attachment"):
                        self.assertIn(task["attachment"], data.ATTACHMENTS)
                    names.append(task["name"])
                self.assertTrue(project["updates"])
            for ticket in customer.get("tickets") or []:
                self.assertIn(ticket["stage"], data.TICKET_STAGES)
        for task in data.ORGANISATION["home_tasks"]:
            self.assertIn(task["stage"], data.HOME_STAGES)

    def test_every_lesson_is_client_free(self):
        forbidden = {c["name"] for c in data.CUSTOMERS} | {c["ref"] for c in data.CUSTOMERS}
        forbidden |= {word for c in data.CUSTOMERS for word in c["name"].split() if len(word) > 4}
        forbidden |= {name for name, _, _ in data.USERS.values()} | {
            name.split()[0] for name, _, _ in data.USERS.values()}
        forbidden.add(data.COMPANY["name"])
        for lesson in data.LESSONS:
            text = " ".join(str(lesson.get(k) or "") for k in ("title", "finding", "solution", "keywords"))
            for word in forbidden:
                self.assertNotIn(word.lower(), text.lower(), f"{lesson['key']} names {word}")
            self.assertIsNone(re.search(r"\b\d{3,}\b", text), f"{lesson['key']} has a number like a record")
        self.assertEqual(len({lesson["key"] for lesson in data.LESSONS}), len(data.LESSONS))
        self.assertEqual(len({lesson["title"] for lesson in data.LESSONS}), len(data.LESSONS))
        duplicates = [lesson for lesson in data.LESSONS if lesson["key"].endswith("_dup")]
        self.assertGreaterEqual(len(duplicates), 2)
        self.assertTrue(all(lesson["state"] == "draft" for lesson in duplicates))
        self.assertTrue(all(lesson["key"][:-4] in {x["key"] for x in data.LESSONS} for lesson in duplicates))

    def test_the_eval_of_the_loader_resolves(self):
        lessons = {lesson["key"] for lesson in data.LESSONS}
        rules = {r["name"] for r in data.ORGANISATION["rules"]}
        rules |= {r["name"] for c in data.CUSTOMERS for r in c["rules"]}
        notes = {(n["kind"], n["name"]) for n in data.ORGANISATION["notes"]}
        notes |= {(n["kind"], n["name"]) for c in data.CUSTOMERS for n in c["notes"]}
        documents = {d["key"] for d in data.ORGANISATION["documents"]} | {
            d["key"] for c in data.CUSTOMERS for d in c["documents"]}
        for question in data.EVAL:
            for want in question["expected"]:
                (kind, ref), = want.items()
                if kind == "lesson":
                    self.assertIn(ref, lessons)
                elif kind == "note":
                    self.assertIn(ref, rules)
                elif kind in ("fact", "procedure"):
                    self.assertIn((kind, ref), notes)
                else:
                    self.assertEqual(kind, "document")
                    self.assertIn(ref, documents)

    def test_the_question_set_names_records_of_the_data(self):
        questions = json.loads((ROOT / "demo" / "questions.json").read_text(encoding="utf-8"))["questions"]
        titles = {
            "lesson": {lesson["title"] for lesson in data.LESSONS},
            "note": {r["name"] for r in data.ORGANISATION["rules"]} | {
                r["name"] for c in data.CUSTOMERS for r in c["rules"]},
            "fact": {n["name"] for n in data.ORGANISATION["notes"] + [n for c in data.CUSTOMERS for n in c["notes"]]
                     if n["kind"] == "fact"},
            "procedure": {n["name"] for n in data.ORGANISATION["notes"] + [
                n for c in data.CUSTOMERS for n in c["notes"]] if n["kind"] == "procedure"},
            "document": {d["name"] for d in data.ORGANISATION["documents"] + [
                d for c in data.CUSTOMERS for d in c["documents"]]},
            "task": {t["name"] for c in data.CUSTOMERS for p in c["projects"] for t in p["tasks"]}
            | {t["name"] for c in data.CUSTOMERS for t in c.get("tickets") or []},
        }
        self.assertGreaterEqual(len(questions), 30)
        for question in questions:
            self.assertIn(question["class"], ("lexical", "keywords", "paraphrase"))
            for want in question["expected"]:
                (kind, title), = want.items()
                self.assertIn(title, titles[kind], question["query"])


if __name__ == "__main__":
    unittest.main()
