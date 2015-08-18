from tealight.logo import move, turn


def drawsquare(size):
  for i in range(4):
    move(size)
    turn(90)

def drawlines(size):
  for i in range(4):
    move(size/8)
    turn(-90)
    move(size)
    turn(90)
    move(size/8)
    turn(90)
    move(size)
    turn(-90)
  
def Chessboard(size):
  drawsquare(size)
  turn(90)
  drawlines(size)
  turn(-90)
  drawlines(size)

Chessboard(128)
  
    
