import math

class Shape:
    def getArea(self):
        pass

    def getPerimeter(self):
        pass

    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return 'Circle, radius={:0.2f}'.format(self.radius)


class Rectangle(Shape):
    def __init__(self, sideA, sideB):
        if sideA < 0 or sideB < 0:
            raise ValueError
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return 2 * self.sideA + 2 * self.sideB

    def __str__(self):
        return 'Rectangle, a={:0.2f}, b={:0.2f}'.format(self.sideA, self.sideB)
    

class Triangle(Shape):
    def __init__(self, sideA, sideB, sideC):
        if sideA < 0 or sideB < 0 or sideC < 0:
            raise ValueError
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def getArea(self):
        sumHalf = (self.sideA + self.sideB + self.sideC) / 2
        return math.sqrt(sumHalf * (sumHalf - self.sideA) * (sumHalf - self.sideB) * (sumHalf - self.sideC))

    def getPerimeter(self):
        return self.sideA + self.sideB + self.sideC

    def __str__(self):
        return 'Triangle, a={:0.2f}, b={:0.2f}, c={:0.2f}'.format(self.sideA, self.sideB, self.sideC)