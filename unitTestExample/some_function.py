import mymodule
from mock import patch


def some_function():
    instance = mymodule.get_user_name()
    return instance.method()


if __name__ == '__main__':
    with patch('mymodule.get_user_name') as mock:
        instance = mock.return_value
        instance.method.return_value = 'the result'
        result = some_function()
        assert result == 'the result'
