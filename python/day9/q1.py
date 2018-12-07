#!/usr/bin/python
class vect:
	def __init__(self,px,py):
		self.x=px
		self.y=py
	def dispv(self):
		print"(%f,%f)"%(self.x,self.y)
	def __add__(self,a):
		newx=self.x+a.x
		newy=self.y+a.y
		return vect(newx,newy)
v1=vect(10,5)
v2=vect(5,10)
v3=v1+v2
v1.dispv()
v2.dispv()
v3.dispv()
