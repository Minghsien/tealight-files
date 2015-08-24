def palindromes():
  for i in range(100,999):
    for j in range(100,999):
      num = str(i*j)
      top = 0
      if num == num[::-1]:
        if num > top:
          top = num
      
  print(top)

palindromes()