 # def is defineis definition. hello_function is function with empty paranthesis.\
# \n We canput the parameters in their. For now we will not pass any parameters.
def hello_func():
    pass  #pass is keyword used for leaving it blank for a moment so it does not cause any error while running code.
hello_func()   #if want to run function we just say hello_fucntion(). we need toput paranthesis at the end of the function in order to execute it.
                # If we dont have paranthesis at the end then actually equal to the hello_function in line 3.(is equa to function itself).
print(hello_func())  #if we run this code it will give us 'None' output because we have not doing with function yet and IT DOES NOT HAVE RETURN VALUE.

#if run this following function then it give us output "hello function!"
#functions are piece of code we can use it again without repeating ourselves.
def heloo_fun():
    print("Hello function!")
heloo_fun()  

#DRY : Dont Repeat yourselves. we should keep our code dry.Put the code into variables and function so that its in  single location

#We first saw that our hello_func function was returning anything from function it was actually equal to None when run the code. 
# So what its means for a function to return something.
# Nowthis is where  function becomes powerfull because it allows us to operate  on some data and then pass the result to whatever called our function.
#What exactly means is that when we execute function it actually going to be equal to RETURN VALUE.
#  So this executed functions here are actually eqqual to the string 'Hello Function'
# So basically think of a our function as a machine that takes input then produces a result.
#  Always focus on what is INPUT and what is RETURN value.
#we can treate our return value as a string function in our example function is returning string"hello function.
# we can treat return value as string and can make our return value as upper case in below example.
def hello_func():
    return 'Hello Function.'
print(hello_func().upper())

#Now we will create parametre 'greeting' and put it in function  within paranthesis.
#Also we will pass 'Hi'  as a string ARGUMENT in print statement.

def hello_func(greeting):
    return '{} Function.'.format(greeting)
print(hello_func('Hi'))   #OUTPUT: HI Function.

# Right now we dont have any default value for our parameter 'greetin'. so that why it is required to pass the argument with print statement.
# So if want to have default value when ever we call function then it follows as below.
# lets have another parameter name and we set name='you' as a default value for our name parameter.

def hello_func(greeting,name='You'):
    return '{}, {} ' .format(greeting, name)
print(hello_func("hi"))    #output: hi, You


def hello_func(greeting,name='You'):
    return '{}, {} ' .format(greeting, name)
print(hello_func("hi", name="Corey")) #output: hi, Corey

#* args and **kwargs basically  its doing is to allowing to us except an arbitrary number of positional or keyword arguments.
# we use it because we dont know that how maany arbitrary numbers are used in
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)



student_info('Math', 'Art', name='John', age=22)

#Now by creating list
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

# This is an example of months per year function
# Number of days per month. First value placeholder for indexing purposes.
#is_leap is a function, which determine  if a year is a leap year. it takes a single argument 'year' 
#The string with 3 quotes """" is known as docstring. Docsring helps documents what  function and class suppose to do.
#

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31] # list month_days of number of days in month

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    # its mathematical expression to calculate leap years.
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)
def days_in_month(year, month):
    """Return number of days in that month in that year."""
    
    if not 1 <= month <=12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2017))
print(is_leap(2020))
print(days_in_month(2017, 2))
