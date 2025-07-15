marks = int(input("Enter marks of student in % : "))

if marks>45 and marks<=100 :
  if marks <=59:
    print("Pass with B grade")
  elif marks <=74  :
    print("Pass with A grade")
  else :
   print("Pass with E Grade")
else :
  print("Failed or invalid % of marks")