class BigNum :
  num1 = 0
  num2 = 0
  num3 = 0  
  def __init__(self, p, q, r):
        self.num1 = p
        self.num2 = q
        self.num3 = r
   
  def findBiggest(self):
        if (self.num1>self.num2) and (self.num1> self.num3) :
            print(self.num1, ' is biggest')
        elif self.num2> self.num3 :
            print(self.num2, ' is biggest')
        else :
            print(self.num3, ' is biggest')

o = BigNum(10, 20, 30)
o.findBiggest()