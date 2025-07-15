marks = int(input("Enter marks of student in % : "))

if marks>45 and marks<=100 :
  if marks <=74:
     if(marks <=59) :
       print("Pass with B grade")
     else:
       print("Pass with A grade")
  else:
    print("Pass with E grade")   

else :
  print("Failed or invalid % of marks")
