from turtle import Turtle
class Pizza(Turtle):
	dx = 0
	dy = 0
	width = 0
	height = 0
	def __init__(self, x , y, dx, dy, width, height):
		Turtle.__init__(self)
		self.pu()
		self.shapesize(10,10)
		self.shape("circle")
		self.dx = dx
		self.dy = dy
		self.width = width
		self.height = height
		self.goto(x,y)

	def get_eaten(self):
		self.ht()

	def move(self):
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx
		newy = oldy + self.dy
		self.goto(newx,newy)

	def left_side(self):
		return self.xcor()-self.width/2
	def right_side(self):
		return self.xcor()+self.width/2
	def top_side(self):
		return self.ycor()+self.height/2
	def bottom_side(self):
		return self.ycor()-self.height/2