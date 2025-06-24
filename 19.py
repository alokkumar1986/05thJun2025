#Numeric Types in Python

a = 10
print(type(a))  # <class 'int'>

b = 10.0
print(type(b))  # <class 'float'>

c = 10+2j
print(type(c))  # <class 'complex'> 

#Type conversion

# int()
# float()
# complex()

a = 10
print(type(a))  # <class 'int'>
b = float(a)
print(b, type(b))  # <class 'float'>
c = complex(a)
print(c, type(c))  # <class 'complex'> 

x = 10.5
print(type(x))  # <class 'float'>
y = int(x)
print(y, type(y))  # 10 <class 'int'>
z = complex(x)
print(z, type(z))  # (10.5+0j) <class '

p = 10+2j
print(type(p))  # <class 'complex'>
q = int(p.real)
print(q, type(q))  
r = float(p.imag)
print(r, type(r))  # 10.0 <class 'float'>
