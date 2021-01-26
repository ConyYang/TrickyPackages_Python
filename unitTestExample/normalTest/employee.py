class Employee:
    """A sample Emplyee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def get_email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def get_fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
