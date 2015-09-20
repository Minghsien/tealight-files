import math

squares = []
for i in range(1,100):
  squares.append(i**2)
def triples():
  triples = []
  for i in squares:
    for j in squares:
      if i+j in squares:
        triples.append([i,j,i+j])
  print(triples)
  return triples
triples = triples()


def triplecheck(triples):
  for each in triples:
    if math.sqrt(each[0]) + math.sqrt(each[1]) + math.sqrt(each[2]) == 1000:
      print(math.sqrt(each[2]))
      print(math.sqrt(each[1]))
      print(math.sqrt(each[0]))


triplecheck(triples)  
  

  