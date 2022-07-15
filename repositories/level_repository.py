from db.run_sql import run_sql

from models.employee import Employee
from models.credentials import Credential
from models.level import Level


def save(level):
    sql = "INSERT INTO levels (name) VALUES(%s) RETURNING *"
    values = [level.name]
    results = run_sql(sql, values)
    level.id = results[0]["id"]
    return level
