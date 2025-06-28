t = (10, 'Car', 25, 10, 23)

#t.append(100)
#t.insert(2, 45)


l = list(t)

l.append(100)
l.insert(2, 45)

t = tuple(l)
print(t)

del t
print(t)  # NameError: name 't' is not defined