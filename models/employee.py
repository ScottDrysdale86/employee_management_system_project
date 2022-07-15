class Employee:
    def __init__(self, _name, _phone, _email, _contract, _start_date, _end_date, _active=True, _id=None):
        self.name = _name
        self.phone = _phone
        self.email = _email
        self.contract = _contract
        self.start_date = _start_date
        self.end_date = _end_date
        self.active = _active
        self.id = _id
