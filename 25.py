#list 

li = [10, 'Car', 24.5, 10, 23]
li1 = list((10, 'Car', 24.5, 10, 23))

print(type(li))  #<class 'list'>
print(type(li1))  #<class 'list'>

#print(li[6])

li[2] = 25
print(li) # 10, Car, 25, 10, 23
