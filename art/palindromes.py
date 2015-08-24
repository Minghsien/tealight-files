def palindromes():
  for i in range(100,999):
    for j in range(100,999):
      num = str(i*j)
      if num == num[::-1]:
      
        print(num)

palindromes()