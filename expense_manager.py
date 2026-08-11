from database import get_connection


class ExpenseManager:

    def add_expense(
        self,
        user_id,
        description,
        amount,
        category,
        expense_date
    ):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO expenses
            (user_id, description, amount, category, expense_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                description,
                amount,
                category,
                expense_date
            )
        )

        connection.commit()
        connection.close()

    def get_expenses(self, user_id):
        connection = get_connection()

        expenses = connection.execute(
            """
            SELECT
                id,
                description,
                amount,
                category,
                expense_date
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

    def get_total_expenses(self, user_id):
        connection = get_connection()

        result = connection.execute(
            """
            SELECT COALESCE(SUM(amount), 0)
            FROM expenses
            WHERE user_id = ?
            """,
            (user_id,)
        ).fetchone()

        connection.close()

        return result[0]

    def get_expense_count(self, user_id):
        connection = get_connection()

        result = connection.execute(
            """
            SELECT COUNT(*)
            FROM expenses
            WHERE user_id = ?
            """,
            (user_id,)
        ).fetchone()

        connection.close()

        return result[0]

    def get_expenses_by_category(self, user_id):
        connection = get_connection()

        results = connection.execute(
            """
            SELECT
                category,
                SUM(amount) AS total
            FROM expenses
            WHERE user_id = ?
            GROUP BY category
            ORDER BY total DESC
            """,
            (user_id,)
        ).fetchall()

        connection.close()

        return results

    def get_recent_expenses(self, user_id, limit=5):
        connection = get_connection()

        results = connection.execute(
            """
            SELECT
                description,
                amount,
                category,
                expense_date
            FROM expenses
            WHERE user_id = ?
            ORDER BY expense_date DESC, id DESC
            LIMIT ?
            """,
            (user_id, limit)
        ).fetchall()

        connection.close()

        return results

