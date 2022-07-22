from import_resolve import import_resolve

import_resolve() # RESOLVES: ModuleNotFoundError
import unittest

from stack import Stack


class TestStack(unittest.TestCase):

    def __init__(self, *kargs, **kwargs) -> None:
        super().__init__(*kargs, **kwargs)
        self.stack = Stack(1)

    def test_isempty(self):

        result = self.stack.isempty()
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
