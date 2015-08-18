from tealight.logo import move, turn
def Chessboard(size):
  for i in range(4):
    move(size)
    turn(90)
  turn(90)
  for i in range(4):
    move(size/8)
    turn(-90)
    move(size)
    turn(90)
    move(size/8)
    turn(90)
    move(size)
    turn(-90)
  move(200)
Chessboard(128)
    
