from unittest import TestCase
from mock import patch
from mocking import test_method


class MockingTestTestCase(TestCase):
    @patch('mocking.get_user_name')
    def test_mock_stubs(self, test_patch):
        test_patch.return_value = 'Mocked This Silly'
        ret = test_method()
        self.assertEqual(ret, 'Mocked This Silly')