#Python dictionary is a container of the unordered set of objects like lists.
#The objects are surrounded by curly braces { }. The items in a dictionary are a comma-separated list of key:value pairs
# where keys and values are Python data type. 
#Each object or value accessed by key and keys are unique in the dictionary. 
#As keys are used for indexing, they must be the immutable type (string, number, or tuple). 
#You can create an empty dictionary using empty curly braces.



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


#sorting of dictionary
ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
sort =sorted(ee_countries.values())[-2]
print(sort)
