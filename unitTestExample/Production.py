from unittest.mock import MagicMock
from unittest.mock import Mock


class ProductionClass:
    def method(self):
        self.something(1,2,3)

    def something(self, a, b, c):
        pass

    def closer(self, something):
        something.close()


# mock Patching Methods
if __name__ == '__main__':
    real = ProductionClass()
    # In most of these examples the Mock and MagicMock classes are interchangeable. As the MagicMock is the more capable class it makes a sensible one to use by default.
    # real.something = MagicMock()
    # real.method()
    # real.something.assert_called_once_with(1, 2, 3)
    mock = Mock()
    real.closer(mock)
    mock.close.assert_called_with()
