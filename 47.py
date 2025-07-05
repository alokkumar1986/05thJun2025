student = {
   'name' : 'ABC',
   'roll' : 120202501,
   'marks' : {
               'math' : 95,
               'scl' : 67,
               'sle' : 87,
               'flo' : 78
             }
}
student = {
   'name' : 'ABC',
   'roll' : 120202501,
   'marks' : {
               'math' : 95,
               'scl' : 67,
               'sle' : 87,
               'flo' : 78
             }
}
# student['marks']['sle'] = 78
# print(student)

# student['marks'].update({'sle': 78})
# print(student)

student.update({ 'marks' : { 'sle' : 78}})
print(student)


print( 100 > 2)

print(int(True))
print(int(False))

print(100 and 2) #2
print(100 or 2) #100

print(100 & 2) #0    
print(100 | 2) #102