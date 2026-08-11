from database import get_connection


class BudgetManager:

    def add_budget(self, user_id, category, amount, month):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO budgets
            (user_id, category, amount, month)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, category, amount, month)
        )

        connection.commit()
        connection.close()

    def get_budgets(self, user_id):
        connection = get_connection()

        budgets = connection.execute(
            """
            SELECT id, category, amount, month
            FROM budgets
            WHERE user_id = ?
            ORDER BY month DESC
            """,
            (user_id,)
        ).fetchall()

        connection.close()

        return budgets

    def delete_budget(self, budget_id, user_id):
        connection = get_connection()

        connection.execute(
            """
            DELETE FROM budgets
            WHERE id = ? AND user_id = ?
            """,
            (budget_id, user_id)
        )

        connection.commit()
        connection.close()