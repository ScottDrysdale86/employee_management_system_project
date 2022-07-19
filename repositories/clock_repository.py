from db.run_sql import run_sql

from models.employee import Employee
from models.clock import Clock

# saves clock
def save(clock):
    sql = "INSERT INTO clocks (day, clock_in, clock_out, employee_id) VALUES(%s,%s,%s, %s) RETURNING *"
    values = [clock.day, clock.clock_in, clock.clock_out, clock.employee.id]
    results = run_sql(sql, values)
    clock.id = results[0]["id"]
    return clock


# returns all clocks
def select_all_clocks():
    clocks = []
    sql = "SELECT * FROM clocks"
    results = run_sql(sql)

    for row in results:
        clock = Clock(row["day"], row["clock_in"], row["clock_out"])
        clocks.append(clock)
    return clocks


# deletes all clocks
def delete_all():
    sql = "DELETE FROM clocks"
    run_sql(sql)


# deletes individual clock based on id
def delete(id):
    sql = "DELETE FROM clocks WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        results = Clock(result["day"], result["clock_in"], result["clock_out"])
    return results


# selects specific clock based on id
def select(id):
    clock = []
    sql = "SELECT * FROM clocks WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        clock = Clock(
            result["day"], result["clock_in"], result["clock_out"], result["id"]
        )
    return clock


# updates clock
def update(clock):
    sql = """UPDATE clocks SET (day, clock_in, clock_out, employee_id) 
    = (%s,%s) WHERE id = %s"""
    values = [clock.day, clock.clock_in, clock.clock_out, clock.employee.id]
    run_sql(sql, values)
