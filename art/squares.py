#difference between the square of the sum and the sum of the sqaures
#(of the first 100 natural numbers)
num = 0
for i in range(101):
  num+=(i*i)
num2 = 0
for i in range(101):
  num2+=(i)
num2=num2*num2
print(num2)
print(num)
print(num2-num)