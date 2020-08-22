import unittest
from CircularLinkedList import *


class MyTestCase(unittest.TestCase):

    # Test print
    def test_list_print(self):
        lista = CircularLinkedList()
        lista.at_start(3)
        lista.at_start(2)
        lista.at_start(1)

        expected = [1, 2, 3]
        self.assertEqual(lista.list_print(), expected)

    # Test at start
    def test_add_start_empty(self):
        lista = CircularLinkedList()
        lista.at_start(5)
        self.assertEqual(lista.list_print(), [5])

    def test_add_start_empty_head(self):
        lista = CircularLinkedList()
        lista.at_start(5)
        self.assertEqual(lista.head.data, 5)

    def test_add_start_empty_tail(self):
        lista = CircularLinkedList()
        lista.at_start(5)
        self.assertEqual(lista.tail.data, 5)

    def test_add_start(self):
        lista = CircularLinkedList()
        lista.at_start(2)
        lista.at_start(1)
        self.assertEqual(lista.list_print(), [1, 2])

    def test_add_start_tail(self):
        lista = CircularLinkedList()
        lista.at_start(2)
        lista.at_start(1)
        self.assertEqual(lista.tail.data, 2)

    def test_add_start_tail_prox_head(self):
        lista = CircularLinkedList()
        lista.at_start(2)
        lista.at_start(1)
        lista.at_start(0)
        self.assertEqual(lista.tail.prox.data, 0)

    # Test at end
    def test_add_end_empty(self):
        lista = CircularLinkedList()
        lista.at_end(5)
        self.assertEqual(lista.list_print(), [5])

    def test_add_end_empty_head(self):
        lista = CircularLinkedList()
        lista.at_end(7)
        self.assertEqual(lista.head.data, 7)

    def test_add_end_empty_tail(self):
        lista = CircularLinkedList()
        lista.at_end(9)
        self.assertEqual(lista.tail.data, 9)

    def test_add_end_empty_tail_prox_head(self):
        lista = CircularLinkedList()
        lista.at_start(13)
        lista.at_end(21)
        lista.at_start(11)
        lista.at_end(9)
        self.assertEqual(lista.tail.prox.data, 11)

    def test_add_end(self):
        lista = CircularLinkedList()
        lista.at_start(5)
        lista.at_end(3)
        self.assertEqual(lista.list_print(), [5, 3])

    def test_add_end_tail(self):
        lista = CircularLinkedList()
        lista.at_start(5)
        lista.at_start(15)
        lista.at_end(3)
        self.assertEqual(lista.tail.data, 3)

    # Test at between
    def test_add_between_empty(self):
        lista = CircularLinkedList()
        lista.at_between(5, 0)
        self.assertEqual(lista.list_print(), [5])

    def test_add_between_empty_head(self):
        lista = CircularLinkedList()
        lista.at_between(8, 0)
        self.assertEqual(lista.head.data, 8)

    def test_add_between_empty_tail(self):
        lista = CircularLinkedList()
        lista.at_between(21, 0)
        self.assertEqual(lista.tail.data, 21)

    def test_add_between_empty_tail_prox_head(self):
        lista = CircularLinkedList()
        lista.at_between(27, 0)
        self.assertEqual(lista.tail.prox.data, 27)

    def test_add_between_start(self):
        lista = CircularLinkedList()
        lista.at_start(1)
        lista.at_between(2, 0)
        self.assertEqual(lista.list_print(), [2, 1])

    def test_add_between_start_head(self):
        lista = CircularLinkedList()
        lista.at_start(41)
        lista.at_between(23, 0)
        self.assertEqual(lista.head.data, 23)

    def test_add_between_start_tail(self):
        lista = CircularLinkedList()
        lista.at_start(63)
        lista.at_between(25, 0)
        self.assertEqual(lista.tail.data, 63)

    def test_add_between_start_tail_prox_head(self):
        lista = CircularLinkedList()
        lista.at_start(26)
        lista.at_between(29, 0)
        self.assertEqual(lista.tail.prox.data, 29)

    def test_add_between_end(self):
        lista = CircularLinkedList()
        lista.at_start(0)  # position 0
        lista.at_end(1)  # position 1
        lista.at_between(2, 2)
        self.assertEqual(lista.list_print(), [0, 1, 2])

    def test_add_between_end_tail(self):
        lista = CircularLinkedList()
        lista.at_start(51)  # position 0
        lista.at_end(13)  # position 1
        lista.at_between(32, 2)
        self.assertEqual(lista.tail.data, 32)

    def test_add_between_end_tail_prox_head(self):
        lista = CircularLinkedList()
        lista.at_start(51)  # position 0
        lista.at_end(13)  # position 1
        lista.at_between(32, 2)
        self.assertEqual(lista.tail.prox.data, 51)

    def test_add_between_valid_position(self):
        lista = CircularLinkedList()
        lista.at_start(0)  # position 0
        lista.at_end(1)  # position 1
        lista.at_end(3)  # position 2
        lista.at_between(2, 2)
        self.assertEqual(lista.list_print(), [0, 1, 2, 3])

    def test_add_between_invalid_position_off_length(self):
        lista = CircularLinkedList()
        lista.at_start(0)  # position 0
        lista.at_end(1)  # position 1
        with self.assertRaisesWithMessage(ValueError):
            lista.at_between(3, 6)  # try to insert at position 6

    def test_add_between_invalid_position_negative(self):
        lista = CircularLinkedList()
        lista.at_start(0)  # position 0
        lista.at_end(1)  # position 1
        with self.assertRaisesWithMessage(ValueError):
            lista.at_between(3, -2)  # try to insert at a negative position

    # Test Remove
    def test_remove(self):
        lista = CircularLinkedList()
        lista.at_start(0)
        lista.at_end(1)
        lista.remove(1)
        self.assertEqual(lista.list_print(), [0])

    def test_remove_all_value(self):
        lista = CircularLinkedList()
        lista.at_start(0)
        lista.at_end(1)
        lista.at_start(1)
        lista.at_end(2)
        # Until this point [1, 0, 1, 2)
        lista.remove(1)
        self.assertEqual(lista.list_print(), [0, 2])  # Test if Remove all "1"

    def test_remove_invalid_value(self):
        lista = CircularLinkedList()
        with self.assertRaisesWithMessage(ValueError):
            lista.remove(None)

    def test_remove_nonexistent_value(self):
        lista = CircularLinkedList()
        lista.at_start(0)
        lista.at_end(1)
        with self.assertRaisesWithMessage(ValueError):
            lista.remove(3)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
