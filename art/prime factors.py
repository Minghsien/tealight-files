def PrimeFactors(num):
  factors = []
  n=2
  while num % n ==0:
    factors.append(n)
    num/=n
    n+=1
  print factors
  
PrimeFactors(13195)