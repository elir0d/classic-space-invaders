import modules.ammo as a
import modules.space_ship as ss

#-----fire----bullet-----#
def fire_bullet():
    if a.bulletstate == "ready":
        a.bulletstate = "fired"
        x = ss.ship.xcor()
        y = ss.ship.ycor() + 10
        a.bullet.setposition(x, y)
        a.bullet.showturtle()

def move_bullet():
    if a.bulletstate == "fired":
        y  = a.bullet.ycor()
        y += a.bulletspeed
        a.bullet.sety(y)

def bullet_colission_check():
    if a.bullet.ycor() > 275:
        a.bullet.hideturtle()
        a.bulletstate = "ready"
