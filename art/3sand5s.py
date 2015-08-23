def sumofmultiples(num,mult):
  add = 0
  for i in range(num//mult):
    if i % mult == 0:
      add+=i
  print add
  
sumofmultiples(10,3)
