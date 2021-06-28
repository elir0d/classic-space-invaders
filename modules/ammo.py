import turtle
import modules.space_ship as ss

#-----bullet-element-----#

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.3, 0.3)
bullet.hideturtle()
bulletspeed = 1
bulletstate = "ready"

#-----move--bullet -----#

