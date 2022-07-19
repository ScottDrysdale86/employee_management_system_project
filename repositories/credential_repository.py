from db.run_sql import run_sql

from models.employee import Employee
from models.credentials import Credential
from models.level import Level

# saves if credential.pin does not already exist.
def save(credential, all_credentials):
    error = False
    for row in all_credentials:
        if int(credential.pin) == row.pin:
            error = True
            return error
    sql = "INSERT INTO credentials (pin, passcode) VALUES(%s,%s) RETURNING *"
    values = [credential.pin, credential.passcode]
    results = run_sql(sql, values)
    credential.id = results[0]["id"]
    return credential


# returns all credentials
def select_all_creds():
    credentials = []
    sql = "SELECT * FROM credentials"
    results = run_sql(sql)

    for row in results:
        credential = Credential(row["pin"], row["passcode"])
        credentials.append(credential)
    return credentials


# deletes all credentials
def delete_all():
    sql = "DELETE FROM credentials"
    run_sql(sql)


# deletes individual credential based on id
def delete(id):
    sql = "DELETE FROM credentials WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        results = Credential(result["pin"], result["passcode"])
    return results


# selects specific credential based on id
def select(id):
    credential = []
    sql = "SELECT * FROM credentials WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        credential = Credential(result["pin"], result["passcode"], result["id"])
    return credential


# selects specific credential based on id
def select_by_pin(pin):
    credential = []
    sql = "SELECT * FROM credentials WHERE pin = %s"
    values = [pin]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        credential = Credential(result["pin"], result["passcode"], result["id"])
    return credential


# updates credential
def update(credential):
    sql = """UPDATE credentials SET (pin, passcode) 
    = (%s,%s) WHERE id = %s"""
    values = [
        credential.pin,
        credential.passcode,
        credential.id,
    ]
    run_sql(sql, values)


# joins 3 tables to then check is pin and passcode matches bd
def check_login_manager(credential):
    entry = False
    sql = """SELECT credentials.pin, credentials.passcode, levels.job_title FROM employees
    JOIN credentials ON employees.credential_id = credentials.id
    JOIN levels ON employees.level_id = levels.id
    WHERE job_title = 'Manager'
    """
    results = run_sql(sql)

    for row in results:
        if (
            int(credential.pin) == row["pin"]
            and int(credential.passcode) == row["passcode"]
        ):
            entry = True
            return entry


# joins 3 tables to then check is pin and passcode matches bd
def check_login_staff(credential):
    entry = False
    sql = """SELECT credentials.id, credentials.pin, credentials.passcode, levels.job_title FROM employees
    JOIN credentials ON employees.credential_id = credentials.id
    JOIN levels ON employees.level_id = levels.id
    WHERE job_title = 'Staff'
    """
    results = run_sql(sql)

    for row in results:
        if (
            int(credential.pin) == row["pin"]
            and int(credential.passcode) == row["passcode"]
        ):
            id = row["id"]
            return id
    return entry
