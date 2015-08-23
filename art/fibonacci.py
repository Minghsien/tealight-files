def fibsum():
  add = 0
  prev = 1
  temp = 0
  current = 1
  while current < 4000000:
    if current % 2 == 0:
      add += current
    temp = current
    current += prev
    prev = temp
    
  print add
       
fibsum()  