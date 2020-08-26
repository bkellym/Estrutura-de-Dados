from Node import *


class CircularLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def list_print(self):
        if self.head:
            retorno = []
            retorno.append(self.head)
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
        # TODO: Método inserir Node início da lista
        return

    def at_end(self, value):
        # TODO: Método inserir Node final da lista
        return

    def at_between(self, value, position):
        # TODO: Método inserir Node na posição informada
        return

    def remove(self, value):
        # TODO: Método remover Node que armazene valor informado
        return
