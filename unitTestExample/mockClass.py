from unittest.mock import Mock,call


def track_al_calls():
    print("track all calls")
    mock = Mock()
    print(mock.method())
    mock.attribute.method(10, x=53)
    print(mock.mock_calls)

    expected = [call.method(), call.attribute.method(10, x=53)]
    print(expected == mock.mock_calls)


def set_return_values_attributes():
    print("Setting Return Values and Attributes")
    mock = Mock()
    mock.return_value = 3
    print(mock())

    mock.method.return_value = 3
    print(mock.method())

    mock.x = 3
    print(mock.x)


def raise_exceptions():
    mock = Mock(side_effect=Exception('Boom!'))
    mock()


if __name__ == '__main__':
    raise_exceptions()