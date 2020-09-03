import unittest
from Pilha import *


class MyTestCase(unittest.TestCase):

    def test_is_Empty_True(self):
        pilha = Pilha()
        self.assertEqual(pilha.isEmpty(), True)

    def test_is_Empty_False(self):
        pilha = Pilha()
        pilha.push(5)
        self.assertEqual(pilha.isEmpty(), False)

    def test_push_value(self):
        pilha = Pilha()
        pilha.push(9)
        self.assertEqual(pilha.list_print(), [9])

    def test_len_not_empty(self):
        pilha = Pilha()
        pilha.push(9)
        pilha.push(3)
        self.assertEqual(pilha.size(), 2)

    def test_len_empty(self):
        pilha = Pilha()
        self.assertEqual(pilha.size(), 0)

    def test_pop_not_empty(self):
        pilha = Pilha()
        pilha.push(7)
        self.assertEqual(pilha.pop(), 7)

    def test_pop_empty(self):
        pilha = Pilha()
        with self.assertRaisesWithMessage(ValueError):
            pilha.pop()

    def test_get_top(self):
        pilha = Pilha()
        pilha.push(7)
        pilha.push(4)
        self.assertEqual(pilha.top(), 4)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()