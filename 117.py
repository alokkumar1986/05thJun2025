from abc import ABC, abstractmethod

class X(ABC):
  
  @abstractmethod
  def fun1(self):
    pass

  def fun2(self):
   print('concrete Method')
 
x = X()  #Error: Can't instantiate abstract class X with abstract methods fun1
