import math

squares = []
for i in range(1,1000):
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
abc = []
for each in triples:
  abc.append([math.sqrt(each[0]),math.sqrt(each[1]),math.sqrt(each[2])])
print abc
for each in abc:
  if (each[0]+each[1]+each[2]) == 1000:
    print each
def triplecheck(triples):
  for each in triples:
    if math.sqrt(each[0]) + math.sqrt(each[1]) + math.sqrt(each[2]) == 1000:
      print(math.sqrt(each[2]))
      print(math.sqrt(each[1]))
      print(math.sqrt(each[0]))


#triplecheck(triples)  
  

  