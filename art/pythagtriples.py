squares = []
for i in range(100):
  squares.append(i**2)
def triples():
  triples = []
  for i in range(len(squares)):
    for each in squares:
      if i+each in squares:
        triples.append(i)
        print(i)
        triples.append(each)
        print(each)
        triples.append(i+each)
        print(i+each)
  print(triples)
print(squares)
triples()
  