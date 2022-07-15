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
