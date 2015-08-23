#prints the even terms of the fibonacci sequence up to a value
def fibsum(num):
  add = 0
  prev = 1
  temp = 0
  current = 1
  while current < num:
    if current % 2 == 0:
      add += current
    temp = current
    current += prev
    prev = temp
    
  print add
       
fibsum(4000000)  