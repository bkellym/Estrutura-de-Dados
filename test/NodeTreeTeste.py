import unittest
from NodeTree import *

class MyTestCase(unittest.TestCase):

    # Create New Node
    def test_create(self):
        self.assertEqual(NodeTree(4).data, 4)

    # Create New Node with None
    def test_create_None(self):
        with self.assertRaisesWithMessage(ValueError):
            NodeTree(None)

    def test_add_left(self):
        node_test = NodeTree(5)
        node_test.left = NodeTree(7)
        self.assertEqual(node_test.left.data, 7)

    def test_add_left_None(self):
        node_test = NodeTree(8)
        node_test.left = None
        self.assertEqual(node_test.left, None)

    def test_add_right(self):
        node_test = NodeTree(9)
        node_test.right = NodeTree(13)
        self.assertEqual(node_test.right.data, 13)

    def test_add_right_None(self):
        node_test = NodeTree(5)
        node_test.right = None
        self.assertEqual(node_test.right, None)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")



if __name__ == '__main__':
    unittest.main()
