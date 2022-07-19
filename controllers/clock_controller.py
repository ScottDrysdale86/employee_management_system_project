
from flask import Flask, render_template, request, redirect, Blueprint
from models.credentials import Credential
from models.employee import Employee
from models.clock import Clock
import repositories.employee_repository as employee_repo
import repositories.credential_repository as cred_repo
import repositories.clock_repository as clock_repo


clocks_blueprint = Blueprint("clocks", __name__)

# loads clock in page
@clocks_blueprint.route("/clocks/new")
def clock_page():
    return render_template("clocks/home.html")


# when add new employee is clicked it saves new employee to the db. Checks is credential already exists
@clocks_blueprint.route("/clocks/new", methods=["POST"])
def add_clock():
    name_id = request.form["name"]
    day = request.form["day"]
    clock_in = request.form["clock_in"]
    clock_out = request.form["clock_out"]
    employee = employee_repo.select(name_id)
    clock = Clock(day, clock_in, clock_out, employee)
    clock_repo.save(clock)

    return redirect("/")

# filter to show all clocks
@clocks_blueprint.route("/clocks/staff")
def show_clocks():
    clocks = clock_repo.select_all_clocks()
    number = len(clocks)
    return render_template(
        "employees/staff-clocks.html", all_clocks=clocks, number=number
    )
