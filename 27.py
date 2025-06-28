#len() : 

l = [10, 'Car', 25, 10, 23]
print(len(l)) #5

#append() :

l = [10, 'Car', 25, 10, 23]
l.append(100)
print(l)  # [10, 'Car', 25, 10, 23, 100]


#insert()
l = [10, 'Car', 25, 10, 23]
l.insert(2, 45)
print(l)  # [10, 'Car', 45, 25, 10, 23]


#remove() :
l = [10, 'Car', 25, 10, 23]
l.remove(10)
print(l)  # ['Car', 25, 10, 23]

#pop() :
l = [10, 'Car', 25, 10, 23]
popedval = l.pop(2)
print(popedval)  # 25
print(l)  # [10, 'Car', 10, 23]

#del() :
l = [10, 'Car', 25, 10, 23]
del l[2]
print(l)  # [10, 'Car', 10, 23]