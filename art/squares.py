num = 0
for i in range(100):
  num+=(i*i)
num2 = 0
for i in range(100):
  num2+=(i)
  num2=num2*num2
  
print(num2-num)