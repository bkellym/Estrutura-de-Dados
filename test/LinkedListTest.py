import unittest
from LinkedList import *


class MyTestCase(unittest.TestCase):

    # Test print
    def test_list_print(self):
        lista = LinkedList()
        lista.at_start(3)
        lista.at_start(2)
        lista.at_start(1)

        expected = [1, 2, 3]
        self.assertEqual(lista.list_print(), expected)

    # Test at start
    def test_add_start_empty(self):
        lista = LinkedList()
        lista.at_start(5)
        self.assertEqual(lista.list_print(), [5])

    def test_add_start(self):
        lista = LinkedList()
        lista.at_start(2)
        lista.at_start(1)
        self.assertEqual(lista.list_print(), [1, 2])

    # Test at end
    def test_add_end_empty(self):
        lista = LinkedList()
        lista.at_end(5)
        self.assertEqual(lista.list_print(), [5])

    def test_add_end(self):
        lista = LinkedList()
        lista.at_start(5)
        lista.at_end(3)
        self.assertEqual(lista.list_print(), [5, 3])

    # Test at between
    def test_add_between_empty(self):
        lista = LinkedList()
        lista.at_between(5, 0)
        self.assertEqual(lista.list_print(), [5])

    def test_add_between_start(self):
        lista = LinkedList()
        lista.at_start(1)
        lista.at_between(2, 0)
        self.assertEqual(lista.list_print(), [2, 1])

    def test_add_between_end(self):
        lista = LinkedList()
        lista.at_start(0)           # position 0
        lista.at_end(1)             # position 1
        lista.at_between(2, 2)
        self.assertEqual(lista.list_print(), [0, 1, 2])

    def test_add_between_valid_position(self):
        lista = LinkedList()
        lista.at_start(0)           # position 0
        lista.at_end(1)             # position 1
        lista.at_end(3)             # position 2
        lista.at_between(2, 2)
        self.assertEqual(lista.list_print(), [0, 1, 2, 3])

    def test_add_between_invalid_position_off_length(self):
        lista = LinkedList()
        lista.at_start(0)   # position 0
        lista.at_end(1)     # position 1
        with self.assertRaisesWithMessage(ValueError):
            lista.at_between(3, 6)      # try to insert at position 6

    def test_add_between_invalid_position_negative(self):
        lista = LinkedList()
        lista.at_start(0)  # position 0
        lista.at_end(1)  # position 1
        with self.assertRaisesWithMessage(ValueError):
            lista.at_between(3, -2)  # try to insert at a negative position

    # Test Remove
    def test_remove(self):
        lista = LinkedList()
        lista.at_start(0)
        lista.at_end(1)
        lista.remove(1)
        self.assertEqual(lista.list_print(), [0])

    def test_remove_all_value(self):
        lista = LinkedList()
        lista.at_start(0)
        lista.at_end(1)
        lista.at_start(1)
        lista.at_end(2)
        # Until this point [1, 0, 1, 2)
        lista.remove(1)
        self.assertEqual(lista.list_print(), [0, 2]) # Test if Remove all "1"

    def test_remove_invalid_value(self):
        lista = LinkedList()
        with self.assertRaisesWithMessage(ValueError):
            lista.remove(None)

    def test_remove_nonexistent_value(self):
        lista = LinkedList()
        lista.at_start(0)
        lista.at_end(1)
        lista.remove(3)
        self.assertEqual(lista.list_print(), [0, 1])


    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
