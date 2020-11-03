class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.last, self.first)

    @property
    def fullname(self):
        return '{}{}'.format(self.last, self.first)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)

emp_1.fullname = 'Wang Nan'
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)
