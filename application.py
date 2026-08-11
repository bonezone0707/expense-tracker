import os
from flask import Flask, render_template, request, redirect, url_for

from database import initialize_database
from expense_manager import ExpenseManager


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

app.config["SECRET_KEY"] = "change-this-secret-key"


initialize_database()

expense_manager = ExpenseManager()


@app.route("/")
def home():
    return """
    <h1>Expense Tracker</h1>
    <p>Welcome to the Expense Tracker application.</p>
    <p><a href="/expenses">Manage Expenses</a></p>
    """


@app.route("/expenses")
def expenses():
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


@app.route("/expenses/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):

    user_id = 1

    expense_manager.delete_expense(
        expense_id,
        user_id
    )

    return redirect(url_for("expenses"))


if __name__ == "__main__":
    app.run(debug=True)