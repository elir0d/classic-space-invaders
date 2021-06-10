import modules.space_ship as ss

#----------Ship-control----------#

def move_left():
    left  = ss.ship.xcor()
    left -= ss.speed
    if left < -280: left = -280 # border checker
    ss.ship.setx(left)

def move_right():
    right  = ss.ship.xcor()
    right += ss.speed
    if right > 280: right = 280 # border checker
    ss.ship.setx(right)

#----------Ship-control----------#