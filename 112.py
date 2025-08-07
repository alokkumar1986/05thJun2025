class Vehicle:
  def move(self) :
    print("Moves")

class Car(Vehicle):
  pass

class Ship:
  def move1(self):
   print("Sail")

class Areoplane(Ship, Car):
  def move2(self):
   print("Fly")


a = Areoplane()

a.move()
a.move1()
a.move2()