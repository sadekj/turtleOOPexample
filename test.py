import turtle

turtle.tracer(0)

x= -100
y= -100
dx=0.1
dy=0.1
turtle.addshape("cat.gif")
turtle.shape("cat.gif")
turtle.pu()
turtle2 = turtle.Turtle()
while(True):
	turtle.goto(x,y)
	turtle.getscreen().update()
	x=x+dx
	y=y+dy


turtle.mainloop()