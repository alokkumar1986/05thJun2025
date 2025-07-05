
d = {
    'name' : 'Aptech',
    'location' : 'Nayapalli',
    'course' : ['Python', 'Django', 'MySQL', 'Angular', 'React', 'Node']
    }

print(d['course']) # ['Python', 'Django', 'MySQL', 'Angular', 'React', 'Node']

print(d['course'][1])  # 'Django'


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

#How to find the mark secured in SLE ?
print(student['marks']) #  { 'math' : 95,'scl' : 67,'sle' : 87, 'flo' : 78 }
print(student['marks']['sle']) # 87