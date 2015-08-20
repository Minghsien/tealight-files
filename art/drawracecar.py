from tealight.art import *
from math import * 
carcolour = "red"
carcentrey = screen_height/2
carcentrex = screen_width/2



def DrawCar(x,y,colour):
  global vertice1, vertice2, vertice3, vertice4
  vertice1 = [x-40,y-25,x-40,y+25]
  vertice2 = [x-40, y-25]
  vertice3 = 
  vertice4 = 
  color(colour)
  line(x,y,x+50,y)
  line(x-40,y-25,x-40,y+25)
  line(x-40,y-25,x,y)
  line(x-40,y+25,x,y)
  line(x-40,y+25,x+50,y)
  line(x-40,y-25,x+50,y)
def handle_keydown(key):
  if key == "left":
    rotation += 3

def rotation(x,y):
  newx = (x - carcentre)*cos(rotation *pi / 180)
  newy = (y - carcentrey)*cos(rotation * pi / 180)
  
def handle_frame():
  colour = "white"
  DrawCar(newx, newy, "red")
DrawCar(carcentrex,carcentrey,carcolour)
#def handle_keydown(key):
#  if key == "left":
#    new
  
#  if key == "right":
  
  
#Drawcar(carcentrex)
  
#newx = (x1 - carcentrex)*cos(rotation * pi / 180)
#newy = (y1 - carcentrey)*cos(rotation * pi / 180)
