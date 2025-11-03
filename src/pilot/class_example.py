# Python code​​​​​​‌‌‌​​‌‌‌​​‌​​‌​‌‌‌‌​‌‌​​‌ below
class Shape:
    width = 5
    height = 5
    printChar = "#"

    def printRow(self, i):
        raise NotImplementedError(
            "Will be implemented by children extending this class"
        )

    def print(self):
        for i in range(self.height):
            self.printRow(i)


class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)


class Triangle(Shape):

    def __init__(self, w, h):
        super().__init__()
        self.width = w
        self.height = h

    def printRow(self, i):
        for i in range(1, self.width +1):
            print(self.printChar * i)

    def print(self):
        for i in range(self.height):
            self.printRow(i)


#t = Triangle(5, 5)
#t.print()
