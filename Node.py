import cv2 as cv


class Node:

    def __init__(self, data: object):
        self.data = data
        self.prox = None

    @property
    def data(self) -> object:
        return self._data

    @data.setter
    def data(self, data: object) -> None:
        if data is None:
            raise ValueError("Not Valid, data is None")

        self._data = data

    @property
    def prox(self):
        return self._prox

    @prox.setter
    def prox(self, node):
        self._prox = node

    def to_string(self):
        print(str(self.data))

    def show_image(self):
        cv.imshow("Photo", self.data)
