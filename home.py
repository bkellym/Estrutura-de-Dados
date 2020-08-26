import cv2 as cv
from CircularLinkedList import CircularLinkedList

lista = CircularLinkedList()

for i in range(1, 5):
    imagem = cv.imread("img/bandeira_" + str(i) + ".png")
    lista.at_end(imagem)

lista.show_slide()
