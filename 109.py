class Vehicle:
  def __init__(self, mk, md):
   self.make = mk
   self.model = md

  def show(self):
   print('Make : ', self.make)
   print('Model : ', self.model)

class Aeroplane(Vehicle):
   def move(self):
     super().show()
     print("It flies")


a = Aeroplane("Indigo", "XT23W")
a.move()