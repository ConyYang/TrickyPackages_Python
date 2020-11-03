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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language


class Manager(Employee):
    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev_1 = Developer('Lucas', 'Satta', 7000, 'Java')
dev_2 = Employee('Nancy', 'Lee', 5000)
print(dev_1.__dict__)
manager_1 = Manager(first='Lotty', last='Sandra', pay=10000, employees=[dev_1])
manager_1.print_employees()
manager_1.add_employee(dev_2)
manager_1.print_employees()
manager_1.remove_employee(dev_1)
manager_1.print_employees()
