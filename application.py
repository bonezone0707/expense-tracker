import os
from flask import Flask, render_template, request, redirect, url_for

from database import initialize_database
from expense_manager import ExpenseManager
from budget_manager import BudgetManager


# --------------------------------------------------
# Application Configuration
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR
)

app.config["SECRET_KEY"] = "change-this-secret-key"


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

initialize_database()


# --------------------------------------------------
# Create Manager Objects
# --------------------------------------------------

expense_manager = ExpenseManager()
budget_manager = BudgetManager()


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Expense Tracker</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 60px auto;
                padding: 20px;
                text-align: center;
            }

            h1 {
                margin-bottom: 10px;
            }

            p {
                margin-bottom: 30px;
            }

            a {
                display: inline-block;
                padding: 12px 20px;
                margin: 10px;
                background-color: #333;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }

            a:hover {
                background-color: #555;
            }
        </style>

    </head>

    <body>

        <h1>Expense Tracker</h1>

        <p>
            Manage your expenses and monthly budgets in one place.
        </p>

        <a href="/expenses">
            Manage Expenses
        </a>

        <a href="/budgets">
            Manage Budgets
        </a>

    </body>

    </html>
    """


# --------------------------------------------------
# Expense Management
# --------------------------------------------------

@app.route("/expenses")
def expenses():

    # Temporary demo user.
    # Authentication will be added later.
    user_id = 1

    expenses_list = expense_manager.get_expenses(user_id)

    return render_template(
        "expenses.html",
        expenses=expenses_list
    )


@app.route("/expenses/add", methods=["POST"])
def add_expense():

    user_id = 1

    description = request.form["description"]
    amount = float(request.form["amount"])
    category = request.form["category"]
    expense_date = request.form["expense_date"]

    expense_manager.add_expense(
        user_id,
        description,
        amount,
        category,
        expense_date
    )

    return redirect(url_for("expenses"))


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

    return redirect(url_for("expenses"))


# --------------------------------------------------
# Budget Management
# --------------------------------------------------

@app.route("/budgets")
def budgets():

    # Temporary demo user.
    # Authentication will be added later.
    user_id = 1

    budgets_list = budget_manager.get_budgets(user_id)

    return render_template(
        "budgets.html",
        budgets=budgets_list
    )


@app.route("/budgets/add", methods=["POST"])
def add_budget():

    user_id = 1

    category = request.form["category"]
    amount = float(request.form["amount"])
    month = request.form["month"]

    budget_manager.add_budget(
        user_id,
        category,
        amount,
        month
    )

    return redirect(url_for("budgets"))


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

    return redirect(url_for("budgets"))


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
