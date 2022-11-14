#For loop : for loop iterates certain number of values
nums = [1,2,3,4,5]

for num in nums:
    print(num)

#use of key words such as break and continiue
nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

#for continue keyword
nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

#Nested loop
nums = [1,2,3,4,5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

#built in function "range"
for i in range(10):
    print(i)  #gives values from 1 to 9 but not 10

#IF we want 10 in output then it follows as below
for i in range(1,11):
    print(i) #gives oupt 1 to 10 but not 11

#while loop : while loop keeps going until certain condition is met or until we hit break
x = 0
while x < 10:
    print(x)
    x += 1

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1    

#infinit loop: if we dont set condtition then its going to be infinite loop
# x = 0
# while True:
#     
#     print(x)
#     x += 1 