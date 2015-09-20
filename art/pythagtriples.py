from math import *

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
triples()


def triplecheck(triples):
  for i in range(len(triples)):
    if i % 3 == 0:
      print(triples[i-2])
      print(triples[i-1])
      print(triples[i])
      if triples[i] + triples[i-1] + triples[i-2] == 10:
        print(triples[i-2])
        print(triples[i-1])
        print(triples[i])

  
  

  