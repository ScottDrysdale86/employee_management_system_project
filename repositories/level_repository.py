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


def delete_all():
    sql = "DELETE FROM levels"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM level WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        level = Level(result["name"], result["id"])
    return level

def select_all_levels():
    levels= []
    sql= "SELECT * FROM levels"
    results =run_sql(sql)

    for row in results:
        level = Level(row["name"], row["id"])
        levels.append(level)
    return levels

def select(id):
    level = []
    sql = "SELECT * FROM levels WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        level = Level(result["name"], result["id"])
    return level
