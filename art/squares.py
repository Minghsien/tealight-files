num = 0
for i in range(10):
  num+=(i*i)
num2 = 0
for i in range(10):
  num2+=(i)
  num2=num2*num2
  
print(num2-num)