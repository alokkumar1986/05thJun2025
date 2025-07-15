list1 = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
n =int(input('Enter a digit from 0 to 9 :'))
try: 
  print(list1[n])
except IndexError:
  print('Invalid digit, please enter a digit from 0 to 9')