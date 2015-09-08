from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
while True:
  if touch() == "fruit":
    move()
    move()
  else:
    if left_side() == "fruit":
      turn(-1)
      move()
      turn(1)
     
  
  
  