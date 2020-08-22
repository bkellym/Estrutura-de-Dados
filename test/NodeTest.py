import unittest
from Node import *


class NodeTest(unittest.TestCase):

    # Create New Node
    def test_create(self):
        self.assertEqual(Node(4).data, 4)

    # Create New Node with None
    def test_create_None(self):
        with self.assertRaisesWithMessage(ValueError):
            Node(None)

    def test_add_prox(self):
        node_test = Node(1)
        node_test.prox = Node(2)
        self.assertEqual(node_test.prox.data, 2)

    def test_add_prox_None(self):
        node_test = Node(1)
        node_test.prox = None
        self.assertEqual(node_test.prox, None)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
