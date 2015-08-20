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
  
theta = 90
def rotatedCar(x,y,colour):
  color(colour)
  line(x,y,cos(theta)*x+50-sin(theta)*y,x*sin(theta)+y*cos(theta))
  line(cos(theta)*(x-40)-sin(theta)*(y-25),(x-40)*sin(theta)+(y-25)*cos(theta),(x-40)*cos(theta)-(y-25)*sin(theta),(x-40)*sin(theta)+(y+25)*cos(theta))
  line((x-40),(y-25),x,y)
  line((x-40),(y+25),x,y)
  line((x-40),(y+25),(x+50),y)
  line((x-40),(y-25),(x+50),y)

def rotation(x,y,theta):
  newx = x*cos(theta)-y*sin(theta)
  newy = x*sin(theta)+y*cos(theta) 
 
  
  
car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]

def rotation2(car, theta):
   theta = math.radians(theta)
   newcar = []
   for vertex in car:
      newcar.append((vertex[0]*cos(theta)-
      vertex[1]*sin(theta),vertex[0]*sin(theta)+
      vertex[1]*cos(theta))
   print(newcar)
                      
    
  
  
  
  
  
#def handle_keydown(key):
#  if key == "left":
#    rotation += 3

#def rotation(x,y):
#  newx = (x - carcentre)*cos(rotation *pi / 180)
#  newy = (y - carcentrey)*cos(rotation * pi / 180)
  
#def handle_frame():
#  colour = "white"
#  DrawCar(newx, newy, "red")
#DrawCar(carcentrex,carcentrey,carcolour)
#def handle_keydown(key):
#  if key == "left":
#    new
  
#  if key == "right":
  
  
#Drawcar(carcentrex)
  
#newx = (x1 - carcentrex)*cos(rotation * pi / 180)
#newy = (y1 - carcentrey)*cos(rotation * pi / 180)
