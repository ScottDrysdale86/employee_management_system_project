import pdb
from models.employee import Employee
from models.credentials import Credential
from models.level import Level
from models.clock import Clock

import repositories.employee_repository as employee_repo
import repositories.credential_repository as cred_repo
import repositories.level_repository as level_repo
import repositories.clock_repository as clock_repo

employee_repo.delete_all()
level_repo.delete_all()
cred_repo.delete_all()

level1 = Level("Staff")
level_repo.save(level1)
level2 = Level("Manager")
level_repo.save(level2)
all_creds = cred_repo.select_all_creds()
credential1 = Credential(1001, 1986)
cred_repo.save(credential1, all_creds)

employee1 = Employee(
    "Will Smith",
    "09876789098",
    "qwerty@qwer.com",
    20,
    "2022-07-07",
    level1,
    credential1,
)
employee_repo.save(employee1)

all_creds = cred_repo.select_all_creds()

credential2 = Credential(1002, 4567)
cred_repo.save(credential2, all_creds)

employee2 = Employee(
    "Dave Grohl",
    "01234566789",
    "qabc@def.com",
    4,
    "2021-12-07",
    level1,
    credential2,
)
employee_repo.save(employee2)

all_creds = cred_repo.select_all_creds()

credential3 = Credential(1003, 5432)
cred_repo.save(credential3, all_creds)

employee3 = Employee(
    "Roger Waters",
    "09876543212",
    "qgoogleadmin@gmail.com",
    40,
    "2020-07-13",
    level2,
    credential3,
)
employee_repo.save(employee3)

all_creds = cred_repo.select_all_creds()
credential4 = Credential(1004, 1234)
cred_repo.save(credential4, all_creds)

employee4 = Employee(
    "Hulk Hogan",
    "09876787678",
    "hulk@hulkamania.co.uk",
    16,
    "2019-09-09",
    level1,
    credential4,
)
employee_repo.save(employee4)

clock1 = clock_repo.Clock("2022-07-14", "10:00", "16:00", employee1)
clock_repo.save(clock1)

clock2 = clock_repo.Clock("2022-07-17", "11:00", "17:00", employee1)
clock_repo.save(clock2)

clock3 = clock_repo.Clock("2022-07-11", "09:00", "17:00", employee1)
clock_repo.save(clock3)

clock4 = clock_repo.Clock("2022-07-20", "12:00", "20:00", employee4)
clock_repo.save(clock4)
