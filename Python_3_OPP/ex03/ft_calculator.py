class calculator:
    def __init__(self, vector):
        """Contructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Make the addtion of a number with a vector"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Make the multiplication of a number with a vector"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Make the substration of a number with a vector"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Make the division of a number with a vector"""
        for x in self.vector:
            if x == 0 & object == 0:
                raise Exception("Cant divide with zero")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
