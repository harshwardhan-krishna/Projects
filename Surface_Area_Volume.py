from twoD_figures import Square, Rectangle, Parallelogram, Trapezium, Circle, Triangle
from threeD_figures import Cuboid


# shape = input(
# 	'**Important Commands**\n # quit "q"\n # help "h"' +
# 	'\n  What is your shape: '
# )

# if shape.lower() == 'square':
# 	ques = input(
# 		'\nWhat do you want to find? (ie, area / peri): '
# 	)

# 	dimension = input('What are your dimensions? (ie, side, 3m or 4cm)')

value = Cuboid(2,5,4)
value.volume()