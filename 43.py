d = { 'name' : 'ABC', 'age': 23, 'course' : 'Python' }

print(type(d))  # <class 'dict'>

d1 = dict(name='ABC', age=23, course= 'Python') 

print(type(d1)) # <class 'dict'>

print(d.keys())

print(d.values())

print(d.items())

for i in d.keys():
    print(i)
    
for j in d.values():
    print(j)
    
for (k, v) in d.items():
    print('Key :', k,', ', 'Value :',v)