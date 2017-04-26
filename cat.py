from turtle import Turtle
class Cat(Turtle):
	name = ''
	age = 0
	favFood = ''
	dx = 0
	dy = 0
	width = 0
	height = 0

	def __init__(self, name, age, favFood, x, y, dx, dy, width, height):
		Turtle.__init__(self)
		self.favFood = favFood
		self.name = name
		self.age = age
		self.shape("circle")
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.width = width
		self.height = height
	def eat(self):
		print(self.name + " is eating "+ self.favFood)

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
