from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# This is a fairly useless algorithm!

while True:
  move()
  
  if touch() == "wall":
    turn(2)
  elif left_side() == "fruit":
    turn(-1)
  elif right_side() == "fruit":
    turn(1)