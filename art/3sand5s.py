def sumofmultiples(num,mult):
  add = 0
  for i in range(0,num):
    if i % mult == 0:
      add+=i
    
      
     
  return add
  
print(sumofmultiples(1000,3)+sumofmultiples(1000,5)-sumofmultiples(1000,15))
print(sumofmultiples(10,3)+sumofmultiples(10,5))
