marks = int(input("Enter marks of student in % : "))

if marks>45 and marks<=60 :
   print('Pass with B Grade')
elif marks >60 and marks<75 :
   print("Pass with A grade")
elif marks>=75 and marks<=100 :
  print("Pass with E Grade")
else :
  print("Failed or invalid % of marks")