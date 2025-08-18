class Vehicle:
  
   def __init__(self,mk, md):
      self.make = mk
      self.model = md

   def move(self):
     print(self.make, " - ", self.model , end="")
     print('Moves')

class Car(Vehicle):
   pass


class Ship(Vehicle):
   def move(self):
      print(self.make, " - ", self.model , end="")
      print('Sails')


obj = Car('Suzuki', 'Baleno')
obj.move()

obj1 = Ship('Indian Coastal Shipping Company', 'A1 Boat')
obj1.move()