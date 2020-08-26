from Node import *


class CircularLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def list_print(self):
        if self.head:
            retorno = []
            retorno.append(self.head.data)
            aux = self.head.prox
            while aux is not self.head:
                retorno.append(aux.data)
                aux = aux.prox
            return retorno
        else:
            raise ValueError("Not Valid, LinkedList is empty")

    def show_slide(self):
        # TODO: Método de listar valores - OpenCV
        return

    def at_start(self, value):
        new_node = Node(value)

        if(self.head):
            new_node.prox = self.head
            self.tail.prox = new_node
        else:
            new_node.prox = new_node
            self.tail = new_node

        self.head = new_node

    def at_end(self, value):
        if self.head is None:
            self.at_start(value)
        else:
            new_node = Node(value)

            new_node.prox = self.head
            self.tail.prox = new_node
            self.tail = new_node

    def at_between(self, value, position):
        if (position < 0) or (self.head is None and position > 0):
            raise ValueError("Position Invalid")

        if position == 0:
            self.at_start(value)
            return

        new_node = Node(value)
        count = 0
        aux = self.head

        while count < position - 1:
            aux = aux.prox
            if aux is self.head:
                break
            count = count + 1

        if aux is self.head:
            raise ValueError("Position Invalid")

        aux_before = aux
        aux = aux.prox

        if self.tail == aux_before:
            self.at_end(value)
            return

        aux_before.prox = new_node
        new_node.prox = aux

    def remove(self, value):
        # TODO: Método remover Node que armazene valor informado
        return
