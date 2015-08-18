from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
while True:
  move()
  if right_side() != "fruit":
    if touch() == "fruit":
      move()
    else:
      turn(-1)
  else:
    turn(-1)
  
  
  