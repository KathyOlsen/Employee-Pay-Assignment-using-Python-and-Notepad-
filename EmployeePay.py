employees = {'Mary':[15.00,40],
'John':[22.00,25],
'Bob':[35.00,4],
'Mel':[43.00,62],
'Jen':[17.00,33],
'Sue':[29.00,45],
'Ken':[40.00,36],
'Dave':[20.00,17],
'Beth':[37.00,37],
'Ray':[16.50,80]}

 
for name,[pay, hours] in employees.items():
    if hours<40:
        salary = pay*hours
    else:
        salary = pay*40 + pay*1.5*(hours-40)
    print(name + ' ', salary)
    

 
 