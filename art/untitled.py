from tealight.art import *
from math import * 
carcolour = "red"
y = screen_height/2
x = screen_width/2

counter = 0 


car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]

def rotation(car, theta):
   theta = math.radians(theta)
   newcar = []
   for vertex in car:
      newcar.append((vertex[0]*cos(theta)-vertex[1]*sin(theta),vertex[0]*sin(theta)+vertex[1]*cos(theta)))

def drawcar(car):
  temppoints = []
  for each in car:
    temppoints.append(each[0])
    temppoints.append(each[1])
    counter += 1
    if counter == 2:
      line(each[0],each[1],each[2],each[3])
      temppoints =[]
      counter = 0

drawcar(car)
      
      
  