# for i in range(1, 101):
#   if i%2 == 0 :
#     print('{} is even'.format(i))
#   else :
#     print('{} is odd'.format(i))


even = []
odd = []

for i in range(1, 101): 
  if i%2 == 0 :
    even.append(i)
  else :
    odd.append(i)

print('even :', even)
print('odd :', odd)