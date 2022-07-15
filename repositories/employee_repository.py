from db.run_sql import run_sql

from models.employee import Employee
from models.credentials import Credential
from models.level import Level


def delete_all():
    sql = "DELETE FROM employees"
    run_sql(sql)


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
