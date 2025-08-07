class Animal: 
   def sound(self): 
     print('Sound')

class Dog(Animal):
   def sound(self):
    print('Bark')

class Shepherd(Dog):
   pass


s = Shepherd()
s.sound()