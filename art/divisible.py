def isdivisable(num,n):
  m=1
  while m< n:
    if num % m == 0:
      m+=1
  if m == n:
    return True
    