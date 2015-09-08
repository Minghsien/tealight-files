from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
while True:
  if touch():
    move()
  else:
    if left_side() == "fruit":
      turn(-1)
  
  
  