from crypt import methods
from flask import Flask, render_template, request, redirect, Blueprint
from models.credentials import Credential
from models.employee import Employee
from models.level import Level
import repositories.employee_repository as employee_repo
import repositories.credential_repository as cred_repo
import repositories.level_repository as level_repo


employees_blueprint = Blueprint("employees", __name__)


@employees_blueprint.route("/employees")
def show_all_employees():
    employees = employee_repo.select_all()
    return render_template("employees/index.html", all_employees=employees)


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


@employees_blueprint.route("/employees", methods=["POST"])
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
    cred_repo.save(credential)
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

    # credential = cred_repo.select(id)
    credential = Credential(pin, passcode, id)
    level = level_repo.select(level_id)

    employee = Employee(name, phone, email, contract, start_date, level, credential, id)
    employee_repo.update(employee)
    cred_repo.update(credential)
    return redirect("/employees")
