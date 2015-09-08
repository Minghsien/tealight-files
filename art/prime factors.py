def PrimeFactors(num):
  factors = []
  n=2
  while num> 1:
    while num % n ==0:
      factors.append(n)
      num/=n
    n+=1
  print factors
  
PrimeFactors(600851475143)
PrimeFactors(9878653432122567887543)