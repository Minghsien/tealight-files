from tealight.art import *

colour = "red"
theta = 90
carcentrey = screen_height/2
carcentrex = screen_width/2



def rotatedCar(x,y,colour,theta):
  color(colour)
  line(x,y,cos(theta)*x+50-sin(theta)*y,x*sin(theta)+y*cos(theta))
  line(cos(theta)*(x-40)-sin(theta)*(y-25),(x-40)*sin(theta)+(y-25)*cos(theta),(x-40)*cos(theta)-(y-25)*sin(theta),(x-40)*sin(theta)+(y+25)*cos(theta))
  
rotatedCar(carcentrex,carcentrey,colour,theta)