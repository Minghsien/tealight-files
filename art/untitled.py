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
      newshape.append((vertex[0]*cos(theta)-vertex[1]*sin(theta),vertex[0]*sin(theta)+vertex[1]*cos(theta)))
   car = newshape
   return car
      
def drawcar(points):
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
rotation(car,90 )
drawcar(car)
      
      
  