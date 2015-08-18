from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
def edge():
  for i in range(32):
    move()
    

for i in range(4):
  edge()
  turn(1)