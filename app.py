from flask import Flask, render_template, redirect, request
import datetime
from controllers.employees_controller import employees_blueprint
from controllers.clocks_controller import clocks_blueprint

app = Flask(__name__)

app.register_blueprint(employees_blueprint)
app.register_blueprint(clocks_blueprint)


@app.route("/")
def home():
    return render_template("login.html")


@app.template_global()
def clock_hours(clock_in, clock_out):
    start_clock = datetime.datetime.combine(datetime.date.today(), clock_in)
    end_clock = datetime.datetime.combine(datetime.date.today(), clock_out)
    difference = end_clock - start_clock
    difference_hours = difference.total_seconds() / 3600
    return difference_hours


if __name__ == "__main__":
    app.run(debug=True)
