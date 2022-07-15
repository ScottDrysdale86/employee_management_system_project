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
    cred_repo.delete(id)


def save(employee):
    sql = """INSERT INTO employees(name, phone, email, contract, start_date,credential_id, level_id) 
    VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING *
    """
    values = [
        employee.name,
        employee.phone,
        employee.email,
        employee.contract,
        employee.start_date,
        employee.credential.id,
        employee.level.id,
    ]
    results = run_sql(sql, values)
    employee.id = results[0]["id"]
    return employee


def select_all():
    employees = []
    sql = "SELECT * FROM employees"
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
