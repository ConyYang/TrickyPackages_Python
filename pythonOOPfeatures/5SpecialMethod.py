class Employee(object):
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

    def __repr__(self):
        return "Employees('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


def test_1():
    dev_2 = Employee('Nancy', 'Lee', 5000)
    print(dev_2.__repr__())
    print(str(dev_2))


def test_2():
    dev_1 = Employee('Nancy', 'Lee', 5000)
    dev_2 = Employee('Liang', 'Lee', 5000)
    print(dev_2 + dev_1)


def test_3():
    dev_1 = Employee('Nancy', 'Lee', 5000)
    print(len(dev_1))


test_3()
