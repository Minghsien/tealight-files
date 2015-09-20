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




  
  

  