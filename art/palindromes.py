def palindromes():
  top = 0
  for i in range(100,999):
    for j in range(100,999):
      num = str(i*j)
      if num == num[::-1]:
        if num > top:
          top = num
      
  print(top)

palindromes()