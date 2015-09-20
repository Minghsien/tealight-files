import math

squares = []
for i in range(1,100):
  squares.append(i**2)
def triples():
  triples = []
  for i in squares:
    for j in squares:
      if i+j in squares:
        triples.append(i)
        triples.append(j)
        triples.append(i+j)
  print(triples)
  return triples
triples = triples()


def triplecheck(triples):
  for i in range(len(triples)):
    if i % 3 == 0:
      print(triples[i-2])
      print(triples[i-1])
      print(triples[i])
      if math.sqrt(triples[i]) + math.sqrt(triples[i-1]) + math.sqrt(triples[i-2]) == 1000:
        print(math.sqrt(triples[i-2]))
        print(math.sqrt(triples[i-1]))
        print(math.sqrt(triples[i]))


#triplecheck(triples)  
  

  