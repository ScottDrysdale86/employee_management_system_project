from db.run_sql import run_sql

from models.employee import Employee
from models.credentials import Credential
from models.level import Level
import repositories.credential_repository as cred_repo
import repositories.employee_repository as employee_repo
import repositories.level_repository as level_repo


def delete_all():
    sql = "DELETE FROM employees"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM employees WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)
    # need to add in if not here
    cred_repo.delete(id)


def save(employee):
    sql = """INSERT INTO employees(name, phone, email, contract, start_date, level_id, credential_id) 
    VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING *
    """
    values = [
        employee.name,
        employee.phone,
        employee.email,
        employee.contract,
        employee.start_date,
        employee.level.id,
        employee.credential.id,
    ]
    results = run_sql(sql, values)
    employee.id = results[0]["id"]

    return employee


def select_all():
    employees = []
    sql = "SELECT * FROM employees ORDER BY id"
    results = run_sql(sql)

    for row in results:
        level = level_repo.select(row["level_id"])
        credential = cred_repo.select(row["credential_id"])
        employee = Employee(
            row["name"],
            row["phone"],
            row["email"],
            row["contract"],
            row["start_date"],
            level,
            credential,
            row["id"],
        )
        employees.append(employee)
    return employees


def select(id):
    employee = None
    sql = "SELECT * FROM employees WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        level = level_repo.select(result["level_id"])
        credential = cred_repo.select(result["credential_id"])

        employee = Employee(
            result["name"],
            result["phone"],
            result["email"],
            result["contract"],
            result["start_date"],
            level,
            credential,
            result["id"],
        )
    return employee


def update(employee):
    sql = """UPDATE employees SET (name, phone, email, contract, start_date, level_id, credential_id) 
    = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"""
    values = [
        employee.name,
        employee.phone,
        employee.email,
        employee.contract,
        employee.start_date,
        employee.level.id,
        employee.credential.id,
        employee.id,
    ]
    run_sql(sql, values)


def select_managers():
    employees =[]
    sql = """SELECT * FROM employees
    INNER JOIN levels
    ON employees.level_id = levels.id
    WHERE levels.name = 'Manager'
    """
    results = run_sql(sql)

    for row in results:
        level = level_repo.select(row["level_id"])
        credential = cred_repo.select(row["credential_id"])
        employee = Employee(
            row["name"],
            row["phone"],
            row["email"],
            row["contract"],
            row["start_date"],
            level,
            credential,
            row["id"],
        )
        employees.append(employee)
    return employees

def select_staff():
    employees =[]
    sql = """SELECT * FROM employees
    INNER JOIN levels
    ON employees.level_id = levels.id
    WHERE levels.name = 'Staff'
    """
    results = run_sql(sql)

    for row in results:
        level = level_repo.select(row["level_id"])
        credential = cred_repo.select(row["credential_id"])
        employee = Employee(
            row["name"],
            row["phone"],
            row["email"],
            row["contract"],
            row["start_date"],
            level,
            credential,
            row["id"],
        )
        employees.append(employee)
    return employees
