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
        # TODO: Método inserir Node final da lista
        return

    def at_between(self, value, position):
        # TODO: Método inserir Node na posição informada
        return

    def remove(self, value):
        # TODO: Método remover Node que armazene valor informado
        return
