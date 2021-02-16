marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

for names in marks:
    print(names, end=' ')
    print(marks[names])

total = 0 
values = []  
for names in marks:
    total += marks[names]
    values.append(marks[names])
avg = total/len(marks)
print(avg)
print(max(values))
print(min(values))

for names in marks:
    if 'J' in names:
        break
    print(names)
    
for names in marks:
    if 'J' in names:
        continue
    print(names)
    
def grades(student):
    for names in marks:
        if names == student:
            return marks[names]
    else:
        print('cannot find this student name')
      
print(grades('Amy'))
        
        
        
        
        