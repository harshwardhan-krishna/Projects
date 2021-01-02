class Cuboid:

	def __init__(self, length, breadth, height):
		self.length = float(length)
		self.breadth = float(breadth)
		self.height = float(height)

	def tsa(self):
		TSA = 2 * (self.length*self.breadth + self.breadth*self.height + self.height*self.length)
		print(TSA)

	def lsa(self):
		LSA = 2 * (self.length+self.breadth)*self.height
		print(LSA)

	def volume(self):
		vol = self.length*self.breadth*self.height
		print(vol)


class Cube:

	def __init__(self, side):
		self.side = float(side)

	def tsa(self):
		tsa = 6 * self.side**2
		print(tsa)

	def lsa(self):
		lsa = 4 * self.side**2

	def volume(self):
		vol = self.side**3
		print(vol)


class Cylinder:

	def __init__(self, radius, height, pi):
		self.radius = radius
		self.height = height

	# def tsa(self):
	# 	tsa = 2 * 
