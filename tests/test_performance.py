import time
import unittest

from expense_manager import ExpenseManager


class TestPerformance(unittest.TestCase):

    def test_expense_retrieval_performance(self):
        manager = ExpenseManager()

        start_time = time.perf_counter()

        for _ in range(100):
            manager.get_recent_expenses(1, limit=5)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(
            f"\n100 expense retrieval operations "
            f"completed in {elapsed_time:.4f} seconds"
        )

        self.assertLess(
            elapsed_time,
            5.0
        )


if __name__ == "__main__":
    unittest.main()
