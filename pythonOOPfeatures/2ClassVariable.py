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


emp1 = Employee('Lucuas', 'GOO', 5000)
emp2 = Employee('Liang', 'Sama', 8000)

emp1.raise_amount = 1.05
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.raise_amount)

print(Employee.num_of_employ)
