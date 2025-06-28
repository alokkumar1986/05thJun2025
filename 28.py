#remove() vs del :

l = [10, 'Car', 25, 10, 23]
l.remove(10)
l.remove('Car')
l.remove(25)
l.remove(23)
print(l)  #[10]
l.remove(10) 
#l.remove(10)  # ValueError: list.remove(x): x not in list
print(l)  #[]

l = [10, 'Car', 25, 10, 23]
del l[0]  # ['Car', 25, 10, 23]
print(l)
del l[1]  # ['Car', 10, 23]
print(l)
del l[2]  # ['Car', 10]
print(l)
#del l[3]  # IndexError: list index out of range
#del l[4]  # IndexError: list index out of range
#del l[5] # IndexError: list index out of range

del l[1]  # ['Car']
print(l)
del l[0]  # []
print(l) #

del l
#print(l) ## NameError: name 'l' is not defined

#extend() : this method is used to add multiple elements to the end of a list.

l = [10, 'Car', 25, 10, 23]
l1 = [100, 200, 300]
l.extend(l1)
print(l)  # [10, 'Car', 25, 10, 23, 100, 200, 300]


l = [10, 'Car', 25, 10, 23]
l1 = [100, 200, 300]
l = l+l1
print(l) # [10, 'Car', 25, 10, 23, 100, 200, 300]

#clear() : this method is used to remove all elements from a list.
l = [10, 'Car', 25, 10, 23]
l.clear()
print(l)  # []