from db.run_sql import run_sql

from models.employee import Employee
from models.credentials import Credential
from models.level import Level


def save(credential):
    sql = "INSERT INTO credentials (pin, passcode) VALUES(%s,%s) RETURNING *"
    values = [credential.pin, credential.passcode]
    results = run_sql(sql, values)
    credential.id = results[0]["id"]
    return credential


def delete_all():
    sql = "DELETE FROM credentials"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM credentials WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        results = Credential(result["pin"], result["passcode"])
    return results


def select(id):
    credential = []
    sql = "SELECT * FROM credentials WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        credential = Credential(result["pin"], result["passcode"], result["id"])
    return credential
