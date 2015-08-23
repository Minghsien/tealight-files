def fibsum():
  add = 0
  old = 1
  temp = 0
  current = 1
  while current < 4000000:
    add += current
    temp = current
    current += old
    old += temp
    
  print add
       
fibsum()  