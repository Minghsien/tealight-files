def fibsum():
  add = 0
  old = 1
  current = 1
  while current < 4000000:
    add += current
    
    current += old
  print add
       
  