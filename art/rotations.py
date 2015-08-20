colour = "red"
theta = 90


def rotatedCar(x,y,colour,theta):
  color(colour)
  line(x,y,cos(theta)*x+50-sin(theta)*y,x*sin(theta)+y*cos(theta))
  line(cos(theta)*(x-40)-sin(theta)*(y-25),(x-40)*sin(theta)+(y-25)*cos(theta),(x-40)*cos(theta)-(y-25)*sin(theta),(x-40)*sin(theta)+(y+25)*cos(theta))
  
rotatedcar(carcentrex,carcentrey,colour,theta)