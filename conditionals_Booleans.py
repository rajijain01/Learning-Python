# comparions:
# Equal:              ==
# Not equal:          !=
# Greaterr than:       >
# Less than:           <
# Greater or Equal     >=
# Less or Equal:       <=
# Boject Identity:     is

# False Values:
#   False 
#   None
#   Zero of any number type
#   Any empty sequence. For example, '',(),[].
#   Any empty mapping. For example, {}.
  
language = 'Python'
if language=='Python':
    print('Language is Python')
else:
    print('no Match')    

#other example For 2 conditions
language1 = 'Java'
if language1=='Python':
    print('Language is Python')
elif language1=='Java':  
    print('Language is Java')
else:
    print('no Match')    

#Booleans operations : and, or, not
user = 'Admin'
logged_in = False
if user =='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#or
user = 'Admin'
logged_in = False
if user =='Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#not
user = 'Admin'
logged_in = False
if  not  logged_in:
    print('Please Log in')
else:
    print('Welcome')

#boolean as a output
a = [1,2,3]
b = [1,2,3]
print(a==b)

#id function in python, as a ad b objects have same values it does not mean that they are same. they both have different ID in python

a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(a is b)

#But if we declare that b==a then they both are same
a = [1,2,3]
b = a

print(id(a))
print(id(b))
print(a is b) # 'is' operator is comparison operator

# False Values:
#   False 
#   None
#   Zero of any number type
#   Any empty sequence. For example, '',(),[].
#   Any empty mapping. For example, {}.

#If we set the condition to False,None and zero then python will evaluate as false
condition = False

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')

condition = None

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')

condition = 0

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')    

#If the condition is set as empty list, tuple, set then python will evaluate as false. other than that is true
#empty list condtion
condition = []

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
#empty tuple condtion
condition = ()

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')

#empty set condtion
condition = {}

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')    
#if the condition is other than empty set,lsits,tuple,zero,false,none than python evaluate as true
condition = 'test'

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')     