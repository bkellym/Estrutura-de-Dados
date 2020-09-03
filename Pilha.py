import cv2 as cv
from Node import *


class Pilha:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def list_print(self):
        if self.head:
            retorno = []
            aux = self.head
            while aux is not None:
                retorno.append(aux.data)
                aux = aux.prox
            return retorno

        else:
            raise ValueError("Not Valid, LinkedList is empty")

    def push(self, value):
        new_node = Node(value)
        new_node.prox = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            raise ValueError("Not Valid, LinkedList is empty")

        value_removed = self.head.data
        self.head = self.head.prox
        return value_removed

    def top(self):
        if not self.head:
            raise ValueError("Not Valid, LinkedList is empty")

        return self.head.data

    def size(self):
        if not self.head:
            return 0

        size = 1
        aux = self.head
        while aux.prox is not None:
            size += 1
            aux = aux.prox

        return size