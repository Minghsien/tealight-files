from tealight.art import *

carcentrey = screen_height/2
carcentrex = screen_width/2
def DrawCar(x,y):
  line(x,y,x+50,y)
  line(x-40,y-25,x-40,y+25)
  line(x-40,y-25,x,y)
  line(x-40,y+25,x,y)
  line(x-40,y+25,x+50,y)
  line(x-40,y-25,x+50,y)
  
DrawCar(carcentrex,carcentrey)
  