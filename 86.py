# funcEven = lambda n : n if n%2==0 else '' 

l = [1, 2, 3, 4, 5, 6]

# l1 = filter(funcEven, l)

l1 = filter(lambda n : n if n%2==0 else '' , l)

for i in l1:
  print(i)