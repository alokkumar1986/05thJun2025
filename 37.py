s = set((10, 'Car', 23.5, 25, 10))

print(s)

s.add(30)

print(s)

#s.add(['Bike', 40])  # This will raise a TypeError because lists are unhashable

s.update(['Bike', 40]) 

print(s)

s.remove(10)

print(s)

pop_item = s.pop()

print("Popped item:", pop_item)
print(s)

#=================================

s.clear()
print(s)

#=================================
s = set((10, 'Car', 23.5, 25, 10))
s.discard('Car')
print(s)

#==================================
del s
print(s)  # NameError: name 's' is not defined