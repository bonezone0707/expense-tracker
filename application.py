import os

from flask import Flask, render_template, request, redirect, url_for

from database import initialize_database
from expense_manager import ExpenseManager
from budget_manager import BudgetManager


# ==========================================================
# APPLICATION CONFIGURATION
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR
)

app.config["SECRET_KEY"] = "change-this-secret-key"


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

initialize_database()


# ==========================================================
# MANAGER OBJECTS
# ==========================================================

expense_manager = ExpenseManager()
budget_manager = BudgetManager()


# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def home():

    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>

        <meta charset="UTF-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <title>Expense Tracker</title>

        <style>

            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 60px auto;
                padding: 20px;
                text-align: center;
                background-color: #f5f5f5;
            }

            h1 {
                margin-bottom: 10px;
            }

            p {
                margin-bottom: 30px;
            }

            .button {
                display: inline-block;
                padding: 12px 20px;
                margin: 10px;
                background-color: #333;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }

            .button:hover {
                background-color: #555;
            }

        </style>

    </head>

    <body>

        <h1>Expense Tracker</h1>

        <p>
            Manage your expenses, budgets, and financial information
            in one place.
        </p>

        <a
            class="button"
            href="/expenses"
        >
            Manage Expenses
        </a>

        <a
            class="button"
            href="/budgets"
        >
            Manage Budgets
        </a>

        <a
            class="button"
            href="/dashboard"
        >
            Financial Dashboard
        </a>

    </body>

    </html>
    """


# ==========================================================
# EXPENSE MANAGEMENT
# ==========================================================

@app.route("/expenses")
def expenses():

    # Temporary demo user.
    # Authentication can be added later.
    user_id = 1

    expenses_list = expense_manager.get_expenses(user_id)

    return render_template(
        "expenses.html",
        expenses=expenses_list
    )


# ----------------------------------------------------------
# ADD EXPENSE
# ----------------------------------------------------------

@app.route("/expenses/add", methods=["POST"])
def add_expense():

    user_id = 1

    description = request.form["description"]

    amount = float(
        request.form["amount"]
    )

    category = request.form["category"]

    expense_date = request.form["expense_date"]

    expense_manager.add_expense(
        user_id,
        description,
        amount,
        category,
        expense_date
    )

    return redirect(
        url_for("expenses")
    )


# ----------------------------------------------------------
# DELETE EXPENSE
# ----------------------------------------------------------

@app.route(
    "/expenses/delete/<int:expense_id>",
    methods=["POST"]
)
def delete_expense(expense_id):

    user_id = 1

    expense_manager.delete_expense(
        expense_id,
        user_id
    )

    return redirect(
        url_for("expenses")
    )


# ==========================================================
# BUDGET MANAGEMENT
# ==========================================================

@app.route("/budgets")
def budgets():

    # Temporary demo user.
    # Authentication can be added later.
    user_id = 1

    budgets_list = budget_manager.get_budgets(
        user_id
    )

    return render_template(
        "budgets.html",
        budgets=budgets_list
    )


# ----------------------------------------------------------
# ADD BUDGET
# ----------------------------------------------------------

@app.route("/budgets/add", methods=["POST"])
def add_budget():

    user_id = 1

    category = request.form["category"]

    amount = float(
        request.form["amount"]
    )

    month = request.form["month"]

    budget_manager.add_budget(
        user_id,
        category,
        amount,
        month
    )

    return redirect(
        url_for("budgets")
    )


# ----------------------------------------------------------
# DELETE BUDGET
# ----------------------------------------------------------

@app.route(
    "/budgets/delete/<int:budget_id>",
    methods=["POST"]
)
def delete_budget(budget_id):

    user_id = 1

    budget_manager.delete_budget(
        budget_id,
        user_id
    )

    return redirect(
        url_for("budgets")
    )


# ==========================================================
# FINANCIAL DASHBOARD
# ==========================================================

@app.route("/dashboard")
def dashboard():

    user_id = 1

    # Get total amount spent
    total_expenses = (
        expense_manager.get_total_expenses(
            user_id
        )
    )

    # Get total amount budgeted
    total_budget = (
        budget_manager.get_total_budget(
            user_id
        )
    )

    # Calculate remaining budget
    remaining_budget = (
        total_budget - total_expenses
    )

    # Get number of expenses
    expense_count = (
        expense_manager.get_expense_count(
            user_id
        )
    )

    # Get spending totals by category
    category_totals = (
        expense_manager.get_expenses_by_category(
            user_id
        )
    )

    # Get the five most recent expenses
    recent_expenses = (
        expense_manager.get_recent_expenses(
            user_id,
            limit=5
        )
    )

    return render_template(
        "dashboard.html",

        total_expenses=total_expenses,

        total_budget=total_budget,

        remaining_budget=remaining_budget,

        expense_count=expense_count,

        category_totals=category_totals,

        recent_expenses=recent_expenses
    )


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )

