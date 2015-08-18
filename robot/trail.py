from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
def search():
  while True:
    move()
    if right_side() == "fruit":
      turn(1)
    elif left_side() == "fruit":
      turn(-1)
    elif look() == "fruit":
      move()
    else:
      turn(1)
search()