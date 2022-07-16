from crypt import methods
from flask import Flask, render_template, request, redirect, Blueprint
from models.employee import Employee
import repositories.employee_repository as employee_repo
import repositories.credential_repository as cred_repo


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


@employees_blueprint.route("/employee/<id>/edit")
def edit_employee(id):
    employee = employee_repo.select(id)
    credential = cred_repo.select(id)
    return render_template(
        "employees/edit.html", employee=employee, credential=credential
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
    return render_template("employees/new.html")


@employees_blueprint.route("/employees", methods=["POST"])
def add_new():

    return redirect("/employees")
