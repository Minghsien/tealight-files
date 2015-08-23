def sumofmultiples(num,mult):
  add = 0
  for i in range(num):
    if i % mult == 0:
      add+=i
  print add
  
sumofmultiples(10,3)
