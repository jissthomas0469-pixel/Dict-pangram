d={}
print(d)
student={'name':'Alvin Jiss',
         'Age' : 13,
         1: 'Math',
         'marks':[78,88,98,32], 
         'addr': {
             'home': 'abc',
             'school' : 'xyz'
        
         },
        1:'music'
    
         }
student['name']='Alvin Octavius Bartholomew Bertram Ignasius Jiss'
print(student)
print(student['name'])

for i in student:
    print(i,student[i])

for i in student.keys():
    print(i)
for i in student.values():
    print(i)
print(student.values())      