class Vehicle:
   def __init__(self, md, mk):
      self.model= md
      self.make = mk  
      
   def __str__(self):
      print(f"Model: {self.model}, Make: {self.make}")

obj = Vehicle('Beleno', 'Suzuki')
print(obj)