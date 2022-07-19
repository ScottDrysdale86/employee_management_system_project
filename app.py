from flask import Flask, render_template, redirect, request
from controllers.employee_controller import employees_blueprint
from controllers.clock_controller import clocks_blueprint

app = Flask(__name__)

app.register_blueprint(employees_blueprint)
app.register_blueprint(clocks_blueprint)



@app.route("/")
def home():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
