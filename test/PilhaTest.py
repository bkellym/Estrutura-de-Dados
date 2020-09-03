import unittest
from Pilha import *


class MyTestCase(unittest.TestCase):

    def __init__(self):
        self.pilha = Pilha()

    def test_is_Empty_True(self):
        self.assertEqual(self.pilha.isEmpty(), True)

    def test_is_Empty_False(self):
        self.pilha.push(5)
        self.assertEqual(self.pilha.isEmpty(), False)

    def test_push_value(self):
        self.assertEqual(self.pilha.list_print(), [5])

    def test_len_not_empty(self):
        self.pilha.push(3)
        self.assertEqual(self.pilha.size(), 2)

    def test_len_empty(self):
        self.pilha.pop()
        self.pilha.pop()
        self.assertEqual(self.pilha.size(), 0)

    def test_pop_not_empty(self):
        self.pilha.push(7)
        self.assertEqual(self.pilha.pop(), 7)

    def test_pop_empty(self):
        with self.assertRaisesWithMessage(ValueError):
            self.pilha.pop()

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()