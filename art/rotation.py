from tealight.art import *
from math import * 
carcolour = "red"
y = screen_height/2
x = screen_width/2


car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]
    

def rotation(shape, theta):
   theta = radians(theta)
   newshape = []
   for vertex in shape:
      print(vertex[0],vertex[1])
      newshape.append((((vertex[0]-x)*cos(theta)-(vertex[1]-y)*sin(theta))+x,((vertex[0]-x)*sin(theta)+(vertex[1]-y)*cos(theta)+y)))
   newcar = newshape
   print(newcar)
   return newcar
      
def drawcar(points,colour):
  color(colour)
  temppoints = []
  counter = 0 
  for each in points:
    temppoints.append(each[0])
    temppoints.append(each[1])
    counter += 1
    if counter == 2:
      line(temppoints[0],temppoints[1],temppoints[2],temppoints[3])
      temppoints =[]
      counter = 0
moved = False 
newcar = rotation(car,0)
drawcar(newcar,"blue")

def handle_keydown(key):
  global newcar
  if key == "left":
    color("white")
    box(0,0,screen_width,screen_height)
      
    #drawcar(newcar,"white")
      
    newcar = rotation(newcar,-10)
    drawcar(newcar,"blue")
  elif key == "right":
    color("white")
    box(0,0,screen_width,screen_height)
    #drawcar(newcar,"white")
      
    newcar = rotation(newcar,10)
    drawcar(newcar,"blue")
        

  #if moved == True:
    
   # drawcar(newcar,"white")
  #elif moved == False:
  #  drawcar(newcar,"blue")
   
