from tealight.art import *
from math import * 
carcolour = "red"
carcentrey = screen_height/2
carcentrex = screen_width/2



def DrawCar(x,y,colour):
  color(colour)
  line(x,y,x+50,y)
  line(x-40,y-25,x-40,y+25)
  line(x-40,y-25,x,y)
  line(x-40,y+25,x,y)
  line(x-40,y+25,x+50,y)
  line(x-40,y-25,x+50,y)

Drawcar(carcentrex,carcentrey,carcolour)
#def handle_keydown(key):
#  if key == "left":
#    new
  
#  if key == "right":
  
  
#Drawcar(carcentrex)
  
#newx = (x1 - carcentrex)*cos(rotation * pi / 180)
#newy = (y1 - carcentrey)*cos(rotation * pi / 180)
