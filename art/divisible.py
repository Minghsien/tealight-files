def isdivisable(num,n):
  m=1
  while m< n:
    if num % m == 0:
      print('y')
      m+=1
  if m == n:
    return('true')
  else:
    return('false')

  
def numbercheck(num, n):
  while isdivisable(num, n) == 'false':
    num+=1
  print(num)
  
  
numbercheck(2520,10)

