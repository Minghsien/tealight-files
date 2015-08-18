from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
while True:
  move()
  while right_side() != "fruit":
    if touch() == "fruit":
      move()
    else:
      turn(-1)
  
  
  