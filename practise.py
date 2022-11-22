# a = 9
# b = 4
# print(a/b)  #a/b: / ; division Quoteint of a nd b : Always meant for floating point arithmetic: for e.g 3.0 or 3.2
# print(a//b) # //: floor divsion : The division of operands where the result is the quotient in which the digits after the decimal point are removed.

# print(a%b) # % : modulus : Remainder of a divided by b

# print(3*(1+2)**2 - (2**2)*3)

# print("what is your nmae")
# # name =input()
# input('name')
# print(name)

# inventory = open("test.txt",'r')
# eof = False
# while eof == False:
#     line = inventory.readline()
#     if line == "":

#         eof = True
#     if line == "\n":

#         continue
#     print(line.strip())

# employee_number = "123-45-6789"
# parts = ""

# while employee_number != "": 
#     valid = False
#     employee_number = input("Enter employee number (ddd-dd-dddd): ")
#     parts = employee_number.split('-')

#     if len(parts) == 3:
#         if len(parts[0]) == 3 and len(parts[1]) == 2 and len(parts[2]) == 4:
#             if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
#                 valid = True


#     print(valid)

# def get_rating(age):
#     rating = ""
#     if age < 13:
#         rating = "c"
#     eif age <18:
#         rating = "t"
#     eif age== None:
#         rating = "c"
#     else:
#         rating = "a"
#     return rating

# a = 3
# b=5
# a += 2**3
# a -=b//2//3
# print(a)


# result = 8//6%5+2**3-2  #8//6%5+8-2,  1%5+8-2, (2**3=8,# 8//6=1,result=1%5+8-2=1+8-2=9-2=7)

# print(result)

# x = 1%5
# print(x)


# s= 'AB CD'
# list=list(s)
# list.append('EF')
# print(list)

# s= 'Python is easy'
# s1=s[-7:]
# s2=s[-4:]
# print(s1+s2)

# x = 'ACROTE'
# y= 'APPLE'
# z = 'TOMATO'
# print(x[2]+y[1]+z[1])
# print(x[-5]+y[0]+z[-2])
# print(x[1]+y[0]+z[0])
# print(x[-5]+y[0]+z[0])

# l=['Apple','Boy','Cat','Dog']
# for x in l:
#    if len(x) == 3:
#       print(x)

# l=['Apple','Boy','Cat','Dog']
# for x in l:
#    if len(x) != 3:
#       print(x)

# l=['Apple','Boy','Cat','Dog']
# for x in l:
#    print(x)

# l=['Apple','Boy','Cat','Dog']
# l1=l[1:]
# for x in l1:
#    print(x)

# for i in (30,40,50):   
#    if i in numbers:
#       x=x+10
# print(x)      

# a=1
# b=2
# c=4
# d=6
# print((b+c//a%d))
# #(2+4)//1%6) = 6//4= 
# print((a+b)//d-c)
# print((a+b)//c*d)
# print((a+b)//c%d)


# ee_countries = {"Croatia": "4.09M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Serbia": "6.8M", "Estonia": "1.3M" }
# ee_countries['Moldova']= '4.1M'
# print(ee_countries)

# set1 = {62, 100, 4001, 82, 550, 4001, 228, 82.0, 21}

# set1.add(450)
# print(set1)


# #A new empty set
# color_set = set()
# #Add a single member
# color_set.add("Red")
# print(color_set)
#  #Add multiple items
# color_set.update(["Blue", "Green"])
# print(color_set)

# #Removing from set
# num_set = set([0, 1, 2, 3, 4, 5])
# num_set.pop()

# print(num_set)
# num_set.pop()

# print(num_set)

# ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
# sort=sorted(ee_countries.values())[-2]
# print(sort)


# mytuple = (150, 350, 400, 250, 600) 
# (a, b, c, d, e) = mytuple
# print(d%10)


#consider code
# values = [[3, 4, 5, 1], [33, 6, 1, 2]]
# v = values[0][0]
# for lst in values:
#    for element in lst:
#       if v > element:
#          v = element
# print(v)

# #We are developing a loan collection agent application. Consider the code:
# #What will be the value of the commission?
# collected_amount=3000
# commission=0
# if collected_amount <= 2000:
#    commission=50
# elif collected_amount> 2500 and collected_amount<3000:
#    commission=100
# elif collected_amount>2500:
#    commission=150
#    if collected_amount>=3000:
#       commission+=200



# #(98-381) Practice Tests Set 1

# Given the list below, answer the following question:

# mylist = ["Europe", "Asia", "North America", "South America", "Africa", "Australia", 2009, 2140, 12.5, 6.25]

# ?What is the result of mylist[2]?


# Options are :

#     North America (Correct)
#     IndexError
#     Asia
#     Africa

# Answer :North America

# Considering the dictionary below (showing the population of some of the Eastern European countries) answer the following question.??

# ee_countries = {"Croatia": "4.09M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Serbia": "6.8M", "Estonia": "1.3M" }??

# Which is the correct way of adding Moldova to the dictionary, having a population of 4.1M?


# Options are :

#     ee_countries["Moldova"] == "4.1M"
#     ee_countries(“Moldova�?) = "4.1M"
#     ee_countries["Moldova"] = "4.1M" (Correct)
#     ee_countries{“Moldova�?} = "4.1M"

# Answer :ee_countries["Moldova"] = "4.1M"

# Given the set below

# ??set1 = {62, 100, 4001, 82, 550, 4001, 228, 82.0, 21}??

# What is the result of set1.add(450)?


# Options are :

#     TypeError and the element doesn’t get added to the set
#     {21, 62, 82, 100, 228, 450, 550, 4001} (Correct)
#     No error, element doesn’t get added to the set.
#     SyntaxError

# Answer :{21, 62, 82, 100, 228, 450, 550, 4001}

# Considering the following string referenced by the fact variable, please select the correct answer to the question below.

# fact = "Values live until nothing references them. Python keeps track of how many references each value has, and automatically cleans up values that have none."

# What is the string method that will turn all lowercase characters to uppercase and vice-versa?


# Options are :

#     fact.capitalize()
#     fact.swapcase() (Correct)
#     fact.casefold()
#     fact.turncase()

# Answer :fact.swapcase()

# Considering the dictionary below (showing the population of some of the Eastern European countries), answer the following question.

# ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"} What is the result of sorted(ee_countries.values())[-2] ?


# Options are :

#     '6.9M' (Correct)
#     '43.7M'
#     SyntaxError
#     '9.6M'

# Answer :'6.9M'

# Given the tuple below, answer the following question.??

# mytuple = (100, 250, 300, 250, 500, 650, 700, 500, 900)??

# How would you find the location (index) of the first occurrence of 500 in mytuple???


# Options are :

#     None of these
#     mytuple.find(500)
#     mytuple.count(500)
#     mytuple.index(500) (Correct)

# Answer :mytuple.index(500)

# Given the code below, answer the following question.

#     ?set1 = {62, 100, 4001, 82, 550, 4001, 228, 82.0, 21}
#     len(set1)

# What is the length of set1?


# Options are :

#     8
#     7 (Correct)
#     6
#     9

# Answer :7
# Which of the following are not valid ways of defining a set?


# Options are :

#     list1 = [24,300,3000,78,400] set1 = set{list1} (Correct)
#     list1 = [24,300,3000,78,400] set1 = set(list1)
#     set1 = [24,300,3000,78,400]
#     list1 = [24,300,3000,78,400] set1 = set[list1] (Correct)

# Answer :list1 = [24,300,3000,78,400] set1 = set{list1} list1 = [24,300,3000,78,400] set1 = set[list1]

# Given the code below, answer the following question.

#     ??mytuple = (150, 350, 400, 250, 600) 
#     (a, b, c, d, e) = mytuple??

# What is the result of d % 10?


# Options are :

#     10
#     0 (Correct)
#     Syntax Error
#     25

# Answer :0

# Considering the dictionary below (showing the population of some of the Eastern European countries) answer the following question.

# ??ee_countries = {"Croatia": "4.09M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Serbia": "6.8M", "Estonia": "1.3M" }??

# Which is the correct way of deleting Estonia from the dictionary?


# Options are :

#     ee_countries["Estonia"].truncate()
#     del ee_countries["Estonia"] (Correct)
#     ee_countries["Estonia"].remove()
#     ee_countries["Estonia"].delete()

# Answer :del ee_countries["Estonia"]

# You created the following program to locate a conference room and display room name.

#     rooms={1:'Left Conference Room',2:'Right Conference Room'}
#     room=input('Enter the room number:')
#     if not room in rooms:#Line-3
#         print('Room does not exist')
#     else:
#         print('The room name is:'+rooms[room])

# Your team reported that the program sometimes produces incorrect results.

# You need to troubleshoot the program. Why does Line-3 Fail to find the rooms?


# Options are :

#     None of these
#     Misnamed variable(s)
#     Invalid Syntax (Correct)
#     The mismatched data type(s)

# Answer :Invalid Syntax

# # Consider the following code:
# def f1(x=0,y=0):
#    return x+y
# # Which of the following method calls are valid?


# # Options are :

# #     f1('10','20') (Correct)
# #     f1('10')
# #     f1(10) (Correct)
# #     f1() (Correct)

# # Answer :f1('10','20') f1(10) f1()

# #(98-381) Practice Tests Set 1

# # 

# employee_number = input('enter your employee number(dd-ddd-ddddd):')
# parts = employee_number.split('_')
# valid = False
# if len(parts) == 3:
#    if len(parts[0])==2 and len(parts[1])==3 and len(parts[2])==4:
#       if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
#          valid=True

# print(valid)

