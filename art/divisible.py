def isdivisable(num,n):
  m=1
  while m< n:
    if num % m == 0:
      print('y')
      m+=1
  if m == n:
    print('True')

isdivisable(2520,10)
