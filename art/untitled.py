car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]

def rotation(car, theta):
   theta = math.radians(theta)
   newcar = []
   for vertex in car:
      newcar.append((vertex[0]*cos(theta)-vertex[1]*sin(theta),vertex[0]*sin(theta)+vertex[1]*cos(theta)))