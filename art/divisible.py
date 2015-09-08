def isdivisable(num,n):
  m=1
  while m< n:
    if num % m == 0:
      print('y')
      m+=1
  if m == n:
    return True
num = 1
while isdivisable(num, 20) == False:
  num+1
  
print(num)
isdivisable(2520,10)