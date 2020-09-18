import unittest
import sys, io
from BinaryTree import *


class MyTestCase(unittest.TestCase):

    # Test print
    def test_first_insert(self):
        binary_tree = BinaryTree()
        binary_tree.insert(8)
        self.assertEqual(binary_tree.head.data, 8)


    def test_insert_left(self):
        binary_tree = BinaryTree()
        binary_tree.insert(8)
        binary_tree.insert(4)
        self.assertEqual(binary_tree.head.left.data, 4)

    def test_insert_right(self):
        binary_tree = BinaryTree()
        binary_tree.insert(8)
        binary_tree.insert(15)
        self.assertEqual(binary_tree.head.right.data, 15)

    def test_inOrderTraverse_empty(self):
        binary_tree = BinaryTree()
        with self.assertRaisesWithMessage(ValueError):
            binary_tree.inOrderTraverse()

    def test_inOrderTraverse_simple(self):
        binary_tree = BinaryTree()
        binary_tree.insert(6)
        binary_tree.insert(1)
        binary_tree.insert(10)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        binary_tree.inOrderTraverse()
        sys.stdout = sys.__stdout__
        self.assertEqual("1\n6\n10\n", captured_output.getvalue())

    def test_inOrderTraverse_complex(self):
        binary_tree = BinaryTree()
        binary_tree.insert(6)
        binary_tree.insert(1)
        binary_tree.insert(10)
        binary_tree.insert(8)
        binary_tree.insert(3)
        binary_tree.insert(12)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        binary_tree.inOrderTraverse()
        sys.stdout = sys.__stdout__
        self.assertEqual("1\n3\n6\n8\n10\n12\n", captured_output.getvalue())

    def test_preOrderTraverse_empty(self):
        binary_tree = BinaryTree()
        with self.assertRaisesWithMessage(ValueError):
            binary_tree.inOrderTraverse()

    def test_preOrderTraverse_simple(self):
        binary_tree = BinaryTree()
        binary_tree.insert(7)
        binary_tree.insert(15)
        binary_tree.insert(4)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        binary_tree.preOrderTraverse()
        sys.stdout = sys.__stdout__
        self.assertEqual("7\n4\n15\n", captured_output.getvalue())

    def test_preOrderTraverse_complex(self):
        binary_tree = BinaryTree()
        binary_tree.insert(7)
        binary_tree.insert(15)
        binary_tree.insert(4)
        binary_tree.insert(2)
        binary_tree.insert(5)
        binary_tree.insert(13)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        binary_tree.preOrderTraverse()
        sys.stdout = sys.__stdout__
        self.assertEqual("7\n4\n2\n5\n15\n13\n", captured_output.getvalue())

    def test_postOrderTraverse_empty(self):
        binary_tree = BinaryTree()
        with self.assertRaisesWithMessage(ValueError):
            binary_tree.postOrderTraverse()

    def test_postOrderTraverse_simple(self):
        binary_tree = BinaryTree()
        binary_tree.insert(9)
        binary_tree.insert(3)
        binary_tree.insert(11)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        binary_tree.postOrderTraverse()
        sys.stdout = sys.__stdout__
        self.assertEqual("11\n3\n9\n", captured_output.getvalue())

    def test_postOrderTraverse_complex(self):
        binary_tree = BinaryTree()
        binary_tree.insert(9)
        binary_tree.insert(3)
        binary_tree.insert(11)
        binary_tree.insert(25)
        binary_tree.insert(7)
        binary_tree.insert(10)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        binary_tree.postOrderTraverse()
        sys.stdout = sys.__stdout__
        self.assertEqual("25\n10\n11\n7\n3\n9\n", captured_output.getvalue())

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

if __name__ == '__main__':
    unittest.main()
