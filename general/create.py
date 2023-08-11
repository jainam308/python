# Python p
# Spiral Helix Pattern
# using Turtle Programming

import turtle
loadWindow = turtle.Screen()
turtle.speed(0)

for i in range(100):
	turtle.circle(1*i)
	turtle.circle(-1*i)
	turtle.left(i)
	turtle.right(19)

turtle.exitonclick()

