import unittest

from expense_manager import ExpenseManager


class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        self.manager = ExpenseManager()
        self.user_id = 1

    def test_get_total_expenses(self):
        total = self.manager.get_total_expenses(self.user_id)
        self.assertIsNotNone(total)
        self.assertGreaterEqual(total, 0)

    def test_get_expense_count(self):
        count = self.manager.get_expense_count(self.user_id)
        self.assertIsNotNone(count)
        self.assertGreaterEqual(count, 0)

    def test_get_expenses_by_category(self):
        categories = self.manager.get_expenses_by_category(self.user_id)
        self.assertIsNotNone(categories)
        self.assertIsInstance(categories, list)

    def test_get_recent_expenses(self):
        expenses = self.manager.get_recent_expenses(
            self.user_id,
            limit=5
        )
        self.assertIsNotNone(expenses)
        self.assertLessEqual(len(expenses), 5)


if __name__ == "__main__":
    unittest.main()
