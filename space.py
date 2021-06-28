#----------Library-----------------#

import os
import sys
import time
import turtle

#----------Modules-----------------#

import modules.ammo         as ammo
import modules.invaders     as invaders
import modules.space_ship   as space_ship
import modules.move_enemy   as move_enemy
import modules.ship_control as ship_control

#----------window setup------------#

window = turtle.Screen()
window.title("Classic Space Invaders")
window.bgcolor("Black")
window.setup(width=700, height=700)
window.tracer(0, 0)

#----------Screen-Border-----------#

border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)

for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

#----------window-changes----------#

window.listen()
window.onkeypress(ship_control.move_left, "a")
window.onkeypress(ship_control.move_right, "d")

#----------Maingame-loop-----------#
def main():
    while True:
        window.update()
        space_ship, invaders, ammo
        move_enemy.move_invader()

if __name__ == "__main__":
    main()