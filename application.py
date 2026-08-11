from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "change-this-secret-key"


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Expense Tracker</title>
    </head>
    <body>
        <h1>Expense Tracker</h1>
        <p>Welcome to the Expense Tracker application.</p>
        <p>The application setup is working correctly.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
