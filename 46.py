d = { 'name' : 'ABC', 'age': 23, 'course' : 'Python'}

print(len(d))

d['name'] = 'PQR'
print(d)

d.update({'name' : 'ABC'})
print(d)
#==================================

d['gender'] = 'male'
print(d)

d.update({'type' : 'general' })
print(d)


d = { 'name' : 'ABC', 'age': 23, 'course' : 'Python'  }

d.pop('age')

print(d)

d = { 'name' : 'ABC', 'age': 23, 'course' : 'Python'  }

d.popitem()

print(d)

#====================================================

d = { 'name' : 'ABC', 'age': 23, 'course' : 'Python'  }
del d['age']

print(d)

#====================================================
d = { 'name' : 'ABC', 'age': 23, 'course' : 'Python'  }
d.clear()
print(d)

print(type(d))  # <class 'dict'>

s = { 10, 23, 'Aptech'}
s.clear()
print(s)
print(type(s))  # <class 'set'>

#=============================================

d = {}
print(d)
print(type(d))  # <class 'dict'> 


d = set()
print(d)
print(type(d))  # <class 'set'>