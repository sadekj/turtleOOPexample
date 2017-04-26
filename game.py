import turtle
from cat import Cat
from pizza import Pizza

turtle.tracer(0)
screen = turtle.getscreen()
turtle.ht()
cat1 = Cat("hello kitty", 3, "Pizza", -300, 0, 1, 0,300,300)
pizza1 = Pizza(100,100,0, 0, 128,128)
turtle.addshape("cat.gif")
turtle.addshape("pizza.gif")
cat1.shape("cat.gif")
pizza1.shape("pizza.gif")

def collide(boxA, boxB):
	if(boxA.top_side() >= boxB.bottom_side() and
		boxA.right_side() >= boxB.left_side() and
		boxA.bottom_side() <= boxB.top_side() and
		boxA.left_side() <= boxB.right_side()):
		return True
	else:
		return False

def upKeyPressed():
	cat1.dy = cat1.dy + 1


screen.onkey(upKeyPressed, "Up")

screen.listen()

while True:
	cat1.move()
	pizza1.move()
	if (collide(cat1,pizza1) ==True):
		pizza1.get_eaten()
	screen.update()
