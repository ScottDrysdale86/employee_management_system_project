from db.run_sql import run_sql

from models.employee import Employee
from models.credentials import Credential
from models.level import Level


def save(level):
    sql = "INSERT INTO levels (job_title) VALUES(%s) RETURNING *"
    values = [level.job_title]
    results = run_sql(sql, values)
    level.id = results[0]["id"]
    return level


def delete_all():
    sql = "DELETE FROM levels"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM levels WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        level = Level(result["job_title"], result["id"])
    return level


def select_all_levels():
    levels = []
    sql = "SELECT * FROM levels"
    results = run_sql(sql)

    for row in results:
        level = Level(row["job_title"], row["id"])
        levels.append(level)
    return levels


def select(id):
    level = []
    sql = "SELECT * FROM levels WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        level = Level(result["job_title"], result["id"])
    return level
