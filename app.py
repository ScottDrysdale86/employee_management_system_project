from flask import Flask, render_template, redirect, request
from controllers.employee_controller import employees_blueprint

app = Flask(__name__)

app.register_blueprint(employees_blueprint)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
