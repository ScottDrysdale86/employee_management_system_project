import pdb
from models.employee import Employee
from models.credentials import Credential
from models.level import Level

import repositories.employee_repository as employee_repo
import repositories.credential_repository as cred_repo
import repositories.level_repository as level_repo

employee_repo.delete_all()
level_repo.delete_all()
cred_repo.delete_all()

level1 = Level("Staff")
level_repo.save(level1)
level2 = Level("Manager")
level_repo.save(level2)

credential1 = Credential(9386, 1986)
cred_repo.save(credential1)

employee1 = Employee(
    "Scott Drysdale",
    "09876789098",
    "qwerty@qwer.com",
    20,
    "2022-07-07",
    level1,
    credential1,
)
employee_repo.save(employee1)


credential2 = Credential(1234, 4567)
cred_repo.save(credential2)

employee2 = Employee(
    "Dave Grohl",
    "01234566789",
    "qabc@def.com",
    4,
    "2022-12-07",
    level1,
    credential2,
)
employee_repo.save(employee2)

credential3 = Credential(9876, 5432)
cred_repo.save(credential3)

employee3 = Employee(
    "Roger Waters",
    "09876543212",
    "qgoogleadmin@gmail.com",
    40,
    "2022-07-13",
    level2,
    credential3,
)
employee_repo.save(employee3)
results = employee_repo.select(2)
print(results.__dict__)
result = level_repo.select(1)
print(result.name)
