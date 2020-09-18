import cv2 as cv


class NodeTree:

    def __init__(self, data: object):
        self.data = data
        self.left = None
        self.right = None

    @property
    def data(self) -> object:
        return self._data

    @data.setter
    def data(self, data: object) -> None:
        if data is None:
            raise ValueError("Not Valid, data is None")

        self._data = data

    def to_string(self):
        print(str(self.data))

    def show_image(self):
        cv.imshow("Photo", self.data)