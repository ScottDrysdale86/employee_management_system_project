from flask import Flask, render_template, request, redirect, Blueprint
from models.employee import Employee
import repositories.employee_repository as employee_repo

employees_blueprint = Blueprint("employees", __name__)


@employees_blueprint.route("/employees")
def show_all_employees():
    employees = employee_repo.select_all()
    return render_template("employees/index.html", all_employees=employees)
