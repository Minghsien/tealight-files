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
    
def smalledge():
  for i in range(4):
    move()
    
def squiggle():
  for i in range(4):
    edge()
    turn(1)
    smalledge()
    turn(1)
    edge()
    turn(-1)
    smalledge()
    turn(-1)
    
def backwardssquiggle():
  for i in range(4):
    edge()
    turn(-1)
    smalledge()
    turn(-1)
    edge()
    turn(1)
    smalledge()
    turn(1)
  
  
  
  
squiggle()
edge()
turn(2)
edge()
turn(1)
squiggle()
edge()

