
from abc import ABC, abstractmethod

class X(ABC):
  
  @abstractmethod
  def fun1(self):
    pass

  def fun2(self):
   print('concrete Method')


class Y(X):
 def fun1(self):
  print('Abstract Method overridden in child')
 

y = Y()
# y.fun1()
y.fun2()