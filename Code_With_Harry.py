class Square:

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        perimeter = self.side*4
        print(perimeter)

    def area(self):
    	area = self.side**2
    	print(area)


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)

    def perimeter(self):
        perimeter = 2 * (self.length * self.width) 
        print(perimeter)


class Parallelogram:

    def __init__(self, side, base, height):
        self.side = side
        self.base = base
        self.height = height

    def area(self):
        area = self.base * self.height
        print(area)

    def perimeter(self):
        perimeter = 2 * (self.side * self.base)
        print(perimeter)


class Trapezium:

    def __init__(self, side1, side2, side3, side4, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.height = height
    
    def area(self):
        area = 0.5 * (self.side2 + self.side4) * self.height
        print(area)
    
    def perimeter(self):
        perimerter = self.side1 + self.side2 + self.side3 + self.side4
        print(perimerter)
    