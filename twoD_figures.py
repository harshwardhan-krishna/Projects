class Square:

    def __init__(self, side):
        self.side = float(side)

    def perimeter(self):
        perimeter = self.side*4
        print(perimeter)

    def area(self):
    	area = self.side**2
    	print(area)


class Rectangle:

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def area(self):
        area = self.length * self.width
        print(area)

    def perimeter(self):
        perimeter = 2 * (self.length * self.width) 
        print(perimeter)


class Parallelogram:

    def __init__(self, side, base, height):
        self.side = float(side)
        self.base = float(base)
        self.height = float(height)

    def area(self):
        area = self.base * self.height
        print(area)

    def perimeter(self):
        perimeter = 2 * (self.side * self.base)
        print(perimeter)


class Trapezium:

    def __init__(self, side1, side2, side3, side4, height):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)
        self.side4 = float(side4)
        self.height = float(height)
    
    def area(self):
        area = 0.5 * (self.side2 + self.side4) * self.height
        print(area)
    
    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3 + self.side4
        print(perimeter)


class Circle:

	def __init__(self, pi, radius):
		self.pi = float(pi)
		self.radius = float(radius)

	def area(self):
		area = self.pi * self.radius**2
		pritn(area)

	def circumference(self):
		circumference = 2 * self.pi * self.radius
		print(circumference)


class Triangle:

	def __init__(self, side1, base, side2, height):
		self.side1 = float(side1)
		self.side2 = float(side2)
		self.base = float(base)
		self.height = float(height)

	def area(self):
		area = self.base * self.height
		print(area)

	def perimeter(self):
		perimeter = self.side1 + self.side2 + self.base
		print(perimeter)
