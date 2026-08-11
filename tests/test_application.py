import unittest

from application import app


class TestApplicationRoutes(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(
            response.status_code,
            200
        )

    def test_expenses_page(self):
        response = self.client.get("/expenses")

        self.assertEqual(
            response.status_code,
            200
        )

    def test_budgets_page(self):
        response = self.client.get("/budgets")

        self.assertEqual(
            response.status_code,
            200
        )

    def test_dashboard_page(self):
        response = self.client.get("/dashboard")

        self.assertEqual(
            response.status_code,
            200
        )


if __name__ == "__main__":
    unittest.main()
