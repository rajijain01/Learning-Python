#Arithemtic Operators:           
# Addition: 3+2
# subtraction: 3 - 2
# Multiply: 3*2
# Division: 3//2
# Exponent : 3 ** 2
# Modulus: 3 % 2

# Order of operators: BODMAS
# B	    Brackets first
# 
# O	    Orders (i.e. Powers and Square Roots, etc.)
#
# DM	Division and Multiplication (left-to-right)
# 
# AS	Addition and Subtraction (left-to-right)

num = 3
#  type is in built function in python which returns data type of object
print(type(num))
#putput class int

num = 3.14
print(type(num))

print(3/2) # ans 1.5
print(3//2)  # ans: 1
print(3**2) # ans: 9
print(3%2)  # ans: 1
print(3 * (2 +1))

# Incremental value

num = 1
num = num + 1
num += 1
print(num) #ans : 

num = 1
num *= 10
print(num)   #ans : 10

#absolute built in function
print(abs(-3)) #ans is 3

#round built in function
print(round(3.75, 1)) #ans: is 3.8

# Comparisons:
# Equal : 3 == 2
# Not Equal : 3!= 2
# Greater THan : 3 > 2
#  Less tha : 3 < 2
# Greater or Equal: 3 >= 2
#  Less or equal: 3 <= 2

num_1 = 3
num_2 = 2
print(num_1 == num_2) #ans: False

num_1 = 3
num_2 = 2
print(num_1 != num_2) #ans: true

num_1 = 3
num_2 = 2
print(num_1 < num_2) #ans: False

num_1 = 3
num_2 = 2
print(num_1 > num_2) #ans: true

num_1 = 3
num_2 = 2
print(num_1 >= num_2) #ans: True

num_1 = 3
num_2 = 2
print(num_1 <= num_2) #ans: False

#variables that looks like number but its actually string 
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)  #ans:100200

# and solve this by casting
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2) #ans: 300
