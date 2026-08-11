import unittest

from budget_manager import BudgetManager


class TestBudgetManager(unittest.TestCase):

    def setUp(self):
        self.manager = BudgetManager()
        self.user_id = 1

    def test_get_total_budget(self):
        total = self.manager.get_total_budget(self.user_id)

        self.assertIsNotNone(total)
        self.assertGreaterEqual(total, 0)

    def test_get_budgets(self):
        budgets = self.manager.get_budgets(self.user_id)

        self.assertIsNotNone(budgets)
        self.assertIsInstance(budgets, list)

    def test_get_budget_count(self):
        budgets = self.manager.get_budgets(self.user_id)

        self.assertGreaterEqual(
            len(budgets),
            0
        )


if __name__ == "__main__":
    unittest.main()
