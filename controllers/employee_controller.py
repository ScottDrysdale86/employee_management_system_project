from flask import Flask, render_template, request, redirect, Blueprint
from models.credentials import Credential
from models.employee import Employee
from models.level import Level
import repositories.employee_repository as employee_repo
import repositories.credential_repository as cred_repo
import repositories.level_repository as level_repo


employees_blueprint = Blueprint("employees", __name__)

# loads log in page
@employees_blueprint.route("/")
def login_form():
    return render_template("login.html")


# when log in is clicked, checked credentials vs DB and either directs to homepage, clock in  or error page
@employees_blueprint.route("/", methods=["POST"])
def login():
    pin = request.form["pin"]
    passcode = request.form["passcode"]
    credential = Credential(pin, passcode)
    manager_result = cred_repo.check_login_manager(credential)
    if manager_result:
        return redirect("/home")
    staff_result = cred_repo.check_login_staff(credential)
    if staff_result != False:
        all_staff = employee_repo.select_staff()
        return render_template("clocks/home.html", all_staff=all_staff)
    return render_template("error.html")


# loads homepage
@employees_blueprint.route("/home")
def show_home():
    return render_template("home.html")


# when view all employees is clicked loads all employees
@employees_blueprint.route("/employees")
def show_all_employees():
    employees = employee_repo.select_all()
    number = len(employees)
    return render_template(
        "employees/employees.html", all_employees=employees, number=number
    )


# when view managers is clicked loads all managers
@employees_blueprint.route("/managers")
def show_managers():
    employees = employee_repo.select_managers()
    number = len(employees)
    return render_template(
        "employees/managers.html", all_employees=employees, number=number
    )


# when view staff is clicked loads all staff
@employees_blueprint.route("/staff")
def show_staff():
    employees = employee_repo.select_staff()
    number = len(employees)
    return render_template(
        "employees/staff.html", all_employees=employees, number=number
    )


# when an employee is clicked it loads individual employee page
@employees_blueprint.route("/employee/<id>")
def show_employee(id):
    employee = employee_repo.select(id)
    credential = cred_repo.select(id)
    return render_template(
        "employees/employee.html", employee=employee, credential=credential
    )


# when delete is clicked loads a delete check page
@employees_blueprint.route("/employee/<id>/delete-check")
def check_delete_employee(id):
    employee = employee_repo.select(id)
    credential = cred_repo.select(id)
    return render_template(
        "employees/delete.html", employee=employee, credential=credential
    )


# if delete is selected at the delete check page. deletes the employee
@employees_blueprint.route("/employee/<id>/delete")
def delete_employee(id):
    employee_repo.delete(id)
    return redirect("/employees")


# loads new employee form page
@employees_blueprint.route("/employees/new")
def new_form():
    levels = level_repo.select_all_levels()
    return render_template("employees/new.html", all_level=levels)


# when add new employee is clicked it saves new employee to the db. Checks is credential already exists
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


# loads edit form
@employees_blueprint.route("/employee/<id>/edit")
def show_edit(id):
    levels = level_repo.select_all_levels()
    employee = employee_repo.select(id)
    return render_template("employees/edit.html", all_levels=levels, employee=employee)


# if update is clicked it updated the db
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
