#math.ceiling(x) : return the ceitling of x, the smallest integer greater than or equal to x.

import math
z = math.ceil(3.2)
print(z)

# math.floor() : # Round numbers down to the nearest integer
print(math.floor(0.6))
a= math.floor(3.2)
print(a)

a = math.floor(4.5)
print(a)

#math.comb(n,k) :Return the number of ways to choose 'k' items fron 'n' items without repetition and without order.
#The math.comb method returns the number of ways picking 'k' unordered outcomes from 'n' possibilities, without repetiton, also known as combinations.
math.comb(3,4)

# math.fabs() : This method returns the absolute value of a number, as a float.
# absolute denotes a non-negative number. This removes the negative sign of the value if it has any.
# This method always converts the value to a float value.

# Remove - sign of given number
print(math.fabs(-66.43))     # output : 66.43
print(math.fabs(-7))         # output: 7.0


# math.factorial() : Returns factorial of a number
# The factorial of a number is the sum of the multiplication, of all the whole numbers,
# from our specified number down to 1. For example, the factorial of 6 would be 6 x 5 x 4 x 3 x 2 x 1 = 720
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))

# math.fmod() : Return the remainder of x/y
print(math.fmod(20, 4))

# math.fsum() : Print the sum of all items
print(math.fsum([1, 2, 3, 4, 5]))

# math.sqrt() : returns the suare root of number
x = math.sqrt(25)
print(x)

# math.isqrt():  Round square root downward to the nearest integer
print (math.isqrt(10))


#math.pow() : 
y = math.pow(4,5)
print(y)

# math.exp() : exponential fo the specified value: Returns E raised to the power of x(E^x)
print(math.exp(65))
print(math.exp(-6.89)) 




#math.pi : returns the value of PI:3.141569
b = math.pi
print(b)

# math.e : returns the eulers number : 2.718
print(math.e)

# math.trnc(): returns the trncated integer parts of different numbers
# Note : this method will not round the number up/down to the nearest integer, but simply remove the decimals.
print(math.trunc(2.77))  # output: 2