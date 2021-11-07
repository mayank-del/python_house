import turtle
t=turtle.Turtle()
def go( x,y):
	t.penup()
	t.go(x,y)
	t.pendown()
	
t.go(-350,-250)
t.lt(90)
t.fd(200)

turtle.done()