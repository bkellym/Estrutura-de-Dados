from NodeTree import *


class BinaryTree:

    def __init__(self):
        self.head: NodeTree = None

    def insert(self, data):
        new_node: NodeTree = NodeTree(data)

        if not self.head:
            self.head = new_node
        else:
            self.insert_leaf(self.head, new_node)

    def insert_leaf(self, node_test: NodeTree, new_node: NodeTree):
        if new_node.data <= node_test.data:
            if not node_test.left:
                node_test.left = new_node
            else:
                self.insert_leaf(node_test.left, new_node)
        else:
            if not node_test.right:
                node_test.right = new_node
            else:
                self.insert_leaf(node_test.right, new_node)

    def inOrderTraverse(self):
        if not self.head:
            raise ValueError("Not Valid, Tree is Empty")
        else:
            self.inOrder(self.head)

    def inOrder(self, node_test: NodeTree):
        if node_test.left:
            self.inOrder(node_test.left)

        node_test.to_string()

        if node_test.right:
            self.inOrder(node_test.right)

    def preOrderTraverse(self):
        if not self.head:
            raise ValueError("Not Valid, Tree is Empty")
        else:
            self.preOrder(self.head)

    def preOrder(self, node_test: NodeTree):
        node_test.to_string()

        if node_test.left:
            self.preOrder(node_test.left)

        if node_test.right:
            self.preOrder(node_test.right)

    def postOrderTraverse(self):
        if not self.head:
            raise ValueError("Not Valid, Tree is Empty")
        else:
            self.postOrder(self.head)

    def postOrder(self, node_test: NodeTree):
        if node_test.right:
            self.postOrder(node_test.right)

        if node_test.left:
            self.postOrder(node_test.left)

        node_test.to_string()
