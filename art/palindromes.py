def palindromes():
  top = 0
  for i in range(10,99):
    for j in range(10,99):
      num = str(i*j)
      print(num)
      if num == num[::-1]:
        if num > top:
          top = num
      
  print(top)

palindromes()