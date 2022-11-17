#create a lists
courses = ['History', 'Maths','Physics','CompSci']
print(courses)

# length(number of objects in list) of the lists
print(len(courses))

#index of the objects in the lists
print(courses[0]) # ans:History
print(courses[3]) #ans:Compsci
#negative index number is always the last item/object in the list
print(courses[-1]) #ans: compsci

#first 2 values form the list,#NOTE:1st index is inclusive but not last index(last index 2 is exclusive)
print(courses[0:2]) 

#if we want to append our course list  method to modify our list
courses.append('Art') #it adds at the end of ther list
print(courses)

#if we want to add in the list between 2 values then it takes 2 arguments
courses.insert(0,'Art') # It adds art at the beginning of the list
print(courses)

#method extend : adds the values to the end of the list and not as list it ads as individual value inthe list
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

#remove items from the lists
courses.remove('Maths')
print(courses)

#by default remove the last item in the list,
courses.pop()
print(courses)
# IF we want the value which is popped out then use popped function 
popped = courses.pop()
print(popped)
print(courses)

#reverse method: it prints out list in the reverse order
courses.reverse()
print(courses)

#sorts method sorts in alphabatical order.It sorts the number in ascending order
courses.sort()
print(courses)

#if we reverse method in sort it will print out reverse order of the lists
courses.sort(reverse=True)
print(courses)

#if we want to sort our list without sorting our original list then we use the sorted function and set as new variable sorted_courses.
sorted_courses = sorted(courses)
print(sorted_courses)

#if we want to check the index of the value in the list then we use index method
print(courses.index('CompSci'))

#operator 'in' is used to check whether the value is present in the lists
print('Art' in courses )

#for loop, item word is variable we can change to anything any word
for item in courses:
    print(item)

#enumerate function returns s2 value index and value
for index, course in enumerate(courses):
    print(index,course)

#if we want to start the list form index value 1 then it follows
for index, course in enumerate(courses,start=1):
    print(index, course)

#string method: we want to convert the list into string then uses join with new variable course_str
course_str = ','.join(courses)   
print(course_str)

#convert the string back to list using split method
new_list = course_str.split(',')
print(new_list)

#TUPLES: major difference is that we cant modify tuples, tuples are immutable.Tuples has parenthesis().we cant append, sorted, remove.
tuple_1 = ('Social Studies', 'Gujarati','Hindi', 'English')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#SETS: Are values that are inordered and also dont have duplicates.It has {} paranthesis.It keeps on changing the ordred of the values.It also usefull whether it shares values with other sets.
cs_courses = {'History','Maths', 'physics', 'CompSci', 'Maths'}
print(cs_courses)

ps_courses = {'History','Maths', 'physics', 'CompSci'}
art_courses = {'History','Maths', 'Art', 'Design'}
print(ps_courses.intersection(art_courses))
print(ps_courses.difference(art_courses))

#union of the sets
print(ps_courses.union(art_courses))

#create empty list
empty_list = []
empty_list = list()

#create empty tuples
empty_tuple =()
empty_tuple = tuple()

#create empty sets
empty_set = {} #This isn't right! its a dictonary
empty_set = set()
 