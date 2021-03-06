from db.run_sql import run_sql
import repositories.employee_repository as employee_repo
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
        employee = employee_repo.select(row["employee_id"])
        clock = Clock(row["day"], row["clock_in"], row["clock_out"], employee)
        clocks.append(clock)
    return clocks


# returns all clocks for last 7 days
def select_clocks_1_week():
    clocks = []
    sql = """SELECT * FROM clocks
    WHERE day BETWEEN current_date-7 AND current_date"""
    results = run_sql(sql)

    for row in results:
        employee = employee_repo.select(row["employee_id"])
        clock = Clock(row["day"], row["clock_in"], row["clock_out"], employee)
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
