from crypt import methods
from flask import Flask, render_template, request, redirect, Blueprint
from models.credentials import Credential
from models.employee import Employee
from models.level import Level
import repositories.employee_repository as employee_repo
import repositories.credential_repository as cred_repo
import repositories.level_repository as level_repo


employees_blueprint = Blueprint("employees", __name__)


@employees_blueprint.route("/")
def login_form():
    return render_template("login.html")


@employees_blueprint.route("/", methods=["POST"])
def login():
    pin = request.form["pin"]
    passcode = request.form["passcode"]
    credential = Credential(pin, passcode)
    result = cred_repo.check_login(credential)
    if result:
        return redirect("/home")
    return render_template("error.html")


@employees_blueprint.route("/home")
def show_home():
    return render_template("index.html")


@employees_blueprint.route("/employees")
def show_all_employees():
    employees = employee_repo.select_all()
    return render_template("employees/index.html", all_employees=employees)


@employees_blueprint.route("/managers")
def show_managers():
    employees = employee_repo.select_managers()
    return render_template("employees/managers.html", all_employees=employees)


@employees_blueprint.route("/staff")
def show_staff():
    employees = employee_repo.select_staff()
    return render_template("employees/staff.html", all_employees=employees)


@employees_blueprint.route("/employee/<id>")
def show_employee(id):
    employee = employee_repo.select(id)
    credential = cred_repo.select(id)
    return render_template(
        "employees/employee.html", employee=employee, credential=credential
    )


@employees_blueprint.route("/employee/<id>/delete-check")
def check_delete_employee(id):
    employee = employee_repo.select(id)
    credential = cred_repo.select(id)
    return render_template(
        "employees/delete.html", employee=employee, credential=credential
    )


@employees_blueprint.route("/employee/<id>/delete")
def delete_employee(id):
    employee_repo.delete(id)
    return redirect("/employees")


@employees_blueprint.route("/employees/new")
def new_form():
    levels = level_repo.select_all_levels()
    return render_template("employees/new.html", all_level=levels)


@employees_blueprint.route("/employees", methods=["GET", "POST"])
def add_new():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    contract = request.form["contract"]
    start_date = request.form["start_date"]
    level_id = request.form["level_id"]
    pin = request.form["pin"]
    passcode = request.form["passcode"]

    credential = Credential(pin, passcode)
    all_credentials = cred_repo.select_all_creds()

    cred_save = cred_repo.save(credential, all_credentials)
    if cred_save == True:
        return render_template("employees/error.html")
    level = level_repo.select(level_id)
    employee = Employee(name, phone, email, contract, start_date, level, credential)
    employee_repo.save(employee)
    return redirect("/employees")


@employees_blueprint.route("/employee/<id>/edit")
def show_edit(id):
    levels = level_repo.select_all_levels()
    employee = employee_repo.select(id)
    return render_template("employees/edit.html", all_levels=levels, employee=employee)


@employees_blueprint.route("/employee/<id>", methods=["POST"])
def update_employee(id):
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    contract = request.form["contract"]
    start_date = request.form["start_date"]
    level_id = request.form["level_id"]
    pin = request.form["pin"]
    passcode = request.form["passcode"]

    credential = Credential(pin, passcode, id)
    level = level_repo.select(level_id)

    employee = Employee(name, phone, email, contract, start_date, level, credential, id)
    employee_repo.update(employee)
    cred_repo.update(credential)
    return redirect("/employees")
