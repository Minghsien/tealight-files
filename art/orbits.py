from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.1
gravity = 0.001
friction = 0.002

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = friction-power
  elif key == "right":
    ax = power-friction
  elif key == "up":
    ay = friction-power
    
  elif key == "down":
    ay = power-friction
    

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  ay+=gravity
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  
