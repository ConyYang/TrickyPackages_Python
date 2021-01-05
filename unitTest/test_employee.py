import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setupClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownClass')

    def setUp(self) -> None:
        print('setUp')
        self.emp_1 = Employee('Cony', 'Yang', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self) -> None:
        print('tearDown')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.get_email, 'Cony.Yang@email.com')
        self.assertEqual(self.emp_2.get_email, 'Sue.Smith@email.com')

        self.emp_1.first = 'Nancy'
        self.emp_2.first = 'Lee'

        self.assertEqual(self.emp_1.get_email, 'Nancy.Yang@email.com')
        self.assertEqual(self.emp_2.get_email, 'Lee.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.get_fullname, 'Cony Yang')
        self.assertEqual(self.emp_2.get_fullname, 'Sue Smith')

        self.emp_1.first = 'Nancy'
        self.emp_2.first = 'Lee'

        self.assertEqual(self.emp_1.get_fullname, 'Nancy Yang')
        self.assertEqual(self.emp_2.get_fullname, 'Lee Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()