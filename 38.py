s = set((10, 'Car', 23.5, 25, 10, 30))
s1 = set([20, 'Bike', 30, 40, 20, 23.5])

s3 = s.union(s1)
print(s3)  

s3 = s | s1
print(s3)

#s.union(s1) = s | s1

s3 = s.intersection(s1)
print(s3)

s3 = s & s1
print(s3)

#s.intersection(s1) = s & s1

s3 = s.difference(s1)
print(s3)

s3 = s - s1
print(s3)

s3 = s.symmetric_difference(s1)
print(s3)

s3 = s ^ s1
print(s3)