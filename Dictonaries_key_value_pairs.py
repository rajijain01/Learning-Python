student = {'name':'John', 'age': 25, 'courses':['Maths', 'Compsci']}
print(student)
print(student['name'])
print(student['courses'])

#get method
print(student.get('phone', 'Not found'))

#to add new key to the dictonaries
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)

#to update multiple values to dictonaries
student.update({'name': 'Mary', 'age':26, 'phone': '666-6666'})
print(student)

#to delete any key in the dictonaries
del student['age']
print(student)

# this is another method to remove the key:
# age = student.pop('age')
# print(student)
# print(age)

# how many keys in our dictonaries
print(len(student))

# to print all keys in our dictonaries
print(student.keys())

#tp print values in our dictonaries
print(student.values())

#keys and values
print(student.items())

for key, value in student.items():
    print(key,value)
    