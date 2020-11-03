class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.co'

    def fullname(self):
        return '{}{}'.format(self.last, self.first)


emp1 = Employee('Lucuas', 'GOO', 5000)
emp2 = Employee('Liang', 'Sama', 8000)

print(emp1.fullname())
print(Employee.fullname(emp2))
