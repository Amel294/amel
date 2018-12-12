import numpy as np
def dist(x1,x2,y1,y2):
	x=(x2-x1)**2
	y=(y2-y1)**2
	z=np.sqrt(x+y)
	print("The distance between points is",z)

dist(input('x1\n'),input('x2\n'),input('y1\n'),input('y2\n'))

