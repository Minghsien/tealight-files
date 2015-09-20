squares = []
for i in range(1,100):
  squares.append(i**2)
def triples():
  triples = []
  for i in squares:
    for j in squares:
      if i+j in squares:
        triples.append(i)
        print(i)
        triples.append(j)
        print(j)
        triples.append(i+j)
        print(i+j)
  print(triples)
  return triples
print(squares)
triples = triples ()
for i in range(len(triples)):
  if i % 3 == 0:
    if triples[i] + triples[i-1] + triples[i-2] == 1000:
      print(triples[i-2])
      print(triples[i-1])
      print(triples[i])
  
  

  