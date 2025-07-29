# funcInt = lambda num : int(num)

l = ['1', '2', '3', '4', '5']

#l = [1, 2, 3, 4, 5]

l1 = map(lambda num : int(num), l)

for i in l1:
    print(i)
# print(l1) #[1, 2, 3, 4, 5]