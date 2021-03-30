def generate(num):
  for i in range(num):
    yield i
    
for i in generate(10):
  print(i)
