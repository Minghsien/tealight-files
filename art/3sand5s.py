def sumofmultiples(num,mult):
  add = 0
  for i in range(num):
    if i % mult == 0:
      add+=i
  return add
  
print(sumofmultiples(1000,3)+sumofmultiples(1000,5))

