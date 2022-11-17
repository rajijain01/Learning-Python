#we will import my_module.py file as intro.py and my_module.py are both in same directories


import my_module

courses = ['History', 'Math', 'Physics', 'Compsci']

index= my_module.find_index(courses, 'Math')
print(index)

#we can specify shorter name for imported my_module
import my_module as mm 

courses = ['History', 'Math', 'Physics', 'Compsci']

index= mm.find_index(courses, 'Math')
print(index)

#import function from the my_module
#It will access to only function but not any other things
from my_module import find_index

courses = ['History', 'Math', 'Physics', 'Compsci']

index= find_index(courses, 'Math')
print(index)

#to check where the modules located
import sys
print(sys.path)
