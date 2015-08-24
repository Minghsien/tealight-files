def palindromes():
  for i in range(100,999):
    for j in range(100,999):
      if str(i*j) == str(i*j)[::-1]):
        print(i*j)

palindromes()