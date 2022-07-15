class Employee:
    def __init__(
        self,
        _name,
        _phone,
        _email,
        _contract,
        _start_date,
        _level,
        _credential,
        _id=None,
    ):
        self.name = _name
        self.phone = _phone
        self.email = _email
        self.contract = _contract
        self.start_date = _start_date
        self.end_date = ""
        self.level = _level
        self.credential = _credential
        self.id = _id
