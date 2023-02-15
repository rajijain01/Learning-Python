# comparions:
# Equal:              ==  : 
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
    print('no Match')      # output = Language is Python

#other example For 2 conditions
language1 = 'Java'
if language1=='Python':
    print('Language is Python')
elif language1=='Java':  
    print('Language is Java')
else:
    print('no Match')      # output: Language is Java

#Booleans operations : and, or, not
user = 'Admin'
logged_in = False
if user =='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')      #output: Bad creds

#or
user = 'Admin'
logged_in = False
if user =='Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')      # output: Admin page 

#not
user = 'Admin'
logged_in = False
if  not  logged_in:
    print('Please Log in')      # output:  Please log in
else:
    print('Welcome')

#boolean as a output
a = [1,2,3]
b = [1,2,3]
print(a==b)                      # output:  True

#id function in python, as a ad b objects have same values it does not mean that they are same. they both have different ID in python

a = [1,2,3]
b = [1,2,3]

print(id(a))                         # output:  140667245995328
print(id(b))                         # output:  140667245652736
print(a is b)                        # output:  false

#But if we declare that b==a then they both are same
a = [1,2,3]
b = a

print(id(a))                      # output: 140667245758976
print(id(b))                      # output : 140667245758976
print(a is b) # 'is' operator is comparison operator         #output : True

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
    print('Evaluate to False')       #Evaluate to False

condition = None

if condition:
    print('Evaluate to True')        
else:
    print('Evaluate to False')        #Evaluate to False

condition = 0

if condition:
    print('Evaluate to True')           
else:
    print('Evaluate to False')           #Evaluate to False

#If the condition is set as empty list, tuple, set then python will evaluate as false. other than that is true
#empty list condtion
condition = []

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')            #Evaluate to False


#empty tuple condtion
condition = ()

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')               #Evaluate to False

# #empty set condtion
condition = {}
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')               #Evaluate to False


#if the condition is other than empty set,lsits,tuple,zero,false,none than python evaluate as true
condition = 'test'
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')                  #Evaluate to False



# In the case of integral values zero 0 treated as False and non-zero treated as True.
#  In the case of float values 0.0  treated as False and all other values (non-zero values) treated as true.
a=bool(0)
b=bool(3)
c=bool(0.5)
d=bool(0.0)

print(a)            #false
print(b)            #true
print(c)            #true
print(d)            #false

#For Empty String, Empty List,Empty tuple,Empty set,Empty dict and range(0) arguments bool() function returns False.

# a= bool([])
# b= bool(())
# c= bool(range(0))
# d= bool({})
# e= bool(set())   

# In boolean expressions:
# 0 is treated as False, non-zero treated as True
# empty string is treated as False and non-empty string treated as True
# None is always treated as False

# print(not 0)   #true
# print(not 10)   #false
# print(not '')   #true
# print(not 'durga')  #false
# print(not None)     #true


# a=15
# b=5
# print(a/b)
