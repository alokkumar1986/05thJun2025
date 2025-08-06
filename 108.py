class Vehicle:
  def __init__(self, mk, md):
   self.make = mk
   self.model = md

  def show(self):
   print('Make : ', self.make)
   print('Model : ', self.model)

class Car(Vehicle) :
  pass


c = Car('Suzuki', 'Baleno')
c.show()