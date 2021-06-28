import turtle
import modules.invaders as invaders

# border check and move enemy
def move_invader():
    x  = invaders.enemy.xcor()
    x += invaders.enemyspeed
    invaders.enemy.setx(x)

    if invaders.enemy.xcor() > 280:
        y  = invaders.enemy.ycor()
        y -= 40
        invaders.enemyspeed *= -1
        invaders.enemy.sety(y)

    if invaders.enemy.xcor() < -280:
        y  = invaders.enemy.ycor()
        y -= 40
        invaders.enemyspeed *= -1
        invaders.enemy.sety(y)