from database import get_connection


class ExpenseManager:

    def add_expense(self, user_id, description, amount, category, expense_date):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO expenses
            (user_id, description, amount, category, expense_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, description, amount, category, expense_date)
        )

        connection.commit()
        connection.close()

    def get_expenses(self, user_id):
        connection = get_connection()

        expenses = connection.execute(
            """
            SELECT id, description, amount, category, expense_date
            FROM expenses
            WHERE user_id = ?
            ORDER BY expense_date DESC
            """,
            (user_id,)
        ).fetchall()

        connection.close()

        return expenses

    def delete_expense(self, expense_id, user_id):
        connection = get_connection()

        connection.execute(
            """
            DELETE FROM expenses
            WHERE id = ? AND user_id = ?
            """,
            (expense_id, user_id)
        )

        connection.commit()
        connection.close()