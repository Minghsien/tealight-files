def palindromes():
  for i in range(100,999):
    for j in range(100,999):
      if i*j == i*j[::-1]:
        print(i*j)

palindromes()