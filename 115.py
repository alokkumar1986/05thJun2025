from multipledispatch import dispatch
class FindSum:  
   @dispatch(int, int)  
   def findSum(self, a, b):
     return a+b 
   
   @dispatch(str, str)  
   def findSum(self, a, b):
     return a+b 
   
   @dispatch(int, int, int)
   def findSum(self, a, b, c):
     return a+b+c
     
obj = FindSum()
print(obj.findSum(10, 20))
print(obj.findSum('Aptech', 'Learning'))
print(obj.findSum(12, 13, 15))
