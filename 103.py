class Person:
  name = ''
  gender = ''
  age  = 0
  def __init__(aptech, n, g, a):
     aptech.name = n
     aptech.gender = g
     aptech.age = a

  def show(aptech):
   print('Name is : ', aptech.name)
   print('Gender :' , aptech.gender)
   print('Age :' , aptech.age)


p = Person('Ram', 'Male', 44)
print(p.name)  #Ram
print(p.gender) #Male
print(p.age)   #44  
p.show()