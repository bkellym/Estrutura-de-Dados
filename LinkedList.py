from Node import *


class LinkedList:

    def __init__(self):
        self.head = None

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

    def show_slide(self):
        # TODO: Método de listar valores - OpenCV
        return

    def at_start(self, value):
        new_node = Node(value)
        new_node.prox = self.head
        self.head = new_node

    def at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        aux = self.head
        while aux.prox is not None:
            aux = aux.prox

        aux.prox = new_node

    def at_between(self, value, position):
        if (position < 0) or (self.head is None and position > 0):
            raise ValueError("Position Invalid")

        if position == 0:
            self.at_start(value)
            return

        new_node = Node(value)
        count = 0
        aux = self.head
        aux_before = None

        while count < position:
            aux_before = aux
            if aux_before is None:
                break
            if aux is not None:
                aux = aux.prox
            count = count + 1

        if aux_before is None:
            raise ValueError("Position Invalid")

        aux_before.prox = new_node
        new_node.prox = aux

    def remove(self, value):
        if value is None:
            raise ValueError("Value Invalid")

        if self.head:
            aux_before = None
            aux = self.head
            while aux is not None:
                if aux.data == value:
                    break
                aux_before = aux
                aux = aux.prox

            if aux is not None:
                if aux_before is None:
                    self.head = aux.prox
                else:
                    aux_before.prox = aux.prox
                self.remove(value)
            else:
                return
        else:
            raise ValueError("Not Valid, List is Empty")
