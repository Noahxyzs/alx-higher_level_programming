#!/usr/bin/python3

class Square:

     def __init__(self, size=0, position=(0, 0)):
         if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

    @property
    def size(self):

        return (self.__size)

    @size.setter
    def size(self, value):
         if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):

        if self._tuple_(value):
            self.__position = value
        elif not self._tuple_(value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def _tuple_(self, position):

        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

    def area(self):

        return (self.size ** 2)

    def my_print(self):

        if self.size == 0:
            print()
            return
        for a in range(self.position[1]):
            print()
        for a in range(self.size):
            print("{}{}".format("0" * self.position[0], "#" * self.size))

    def __str__(self):
        if self.size == 0:
            return ("")
        _sq_str = ""
        for x in range(self.position[1]):
            _sq_str += "\n"
        for i in range(self.size):
            for y in range(self.position[0]):
                _sq_str += " "
            for a in range(self.size):
                _sq_str += "#"
            if i < self.size - 1:
                _sq_str += "\n"
        return (_sq_str)
