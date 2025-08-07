class Animal: 
   def sound(self): 
     print('Sound')

class Dog:
   def sound(self):
     print('Bark')

class Shepherd(Dog, Animal):
   pass


s = Shepherd()
s.sound()