import datetime


class Employee:
    raise_amount = 1.04
    num_of_employ = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.co'
        Employee.num_of_employ += 1

    def fullname(self):
        return '{}{}'.format(self.last, self.first)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def check_weekday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        else:
            return True


emp1 = Employee('Lucuas', 'GOO', 5000)
emp2 = Employee('Liang', 'Sama', 8000)


def test_funct1():
    emp1.set_raise_amount(1.05)
    print(emp1.__dict__)
    print(emp1.raise_amount)


def test_funct2():
    emp_str_1 = 'John-Nasy-8900'
    new_emp = Employee.from_string(emp_str_1)
    print(new_emp.__dict__)


def test_funct3():
    my_date = datetime.date(year=2020, month=7, day=23)
    print(Employee.check_weekday(my_date))
