import unittest
from .solution import InMemoryDB


class SolutionTests(unittest.TestCase):

    def test_level_1(self):
        db = InMemoryDB()

        db.Set("user1", "age", "30")
        db.Set("user1", "age", "31")

        self.assertEqual(db.Get("user1", "name"), "Alice")
        self.assertEqual(db.Get("user1", "age"), "31")

