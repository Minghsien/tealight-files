from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
def search():
  while True:
    if touch() =="fruit":
      move()
    elif right_side() == "fruit":
      turn(1)
      move()
    elif left_side() == "fruit":
      turn(-1)
      move()
    elif look() == "fruit":
      move()
    else:
      turn(1)
      search()
search()