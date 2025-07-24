def showNum(n):
   print(n)
   if n>0:
    n-=1
    showNum(n)


showNum(10)