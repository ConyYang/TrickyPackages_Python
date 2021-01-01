import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Cony', 'Yang', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.get_email, 'Cony.Yang@email,com')
        self.assertEqual(emp_2.get_email, 'Sue.Smith@email.com')

        emp_1.first = 'Nancy'
        emp_2.first = 'Lee'

        self.assertEqual(emp_1.get_email, 'Nancy.Yang@email.com')
        self.assertEqual(emp_2.get_email, 'Lee.Smith@email.com')

    def test_fullname(self):
        pass
