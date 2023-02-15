
import random

# value = random.random()
# print(value)

# valu = random.uniform(1,10)
# print(valu)

value = random.randint(1,6)
print(value)

greetings = ['hello','hi', 'hey', 'howdy','hola']

value = random.choice(greetings)
print(value + ', Corey!')


# random.range() : The randrange() method returns a randomly selected element from the specified range.
# returns a number between 3 (included) and 9 (not included)
print(random.randrange(3, 9))

# random.randint() : The randint() method returns an integer number sselected element from the specified range.
# returns a number between 3 and 9 (both included)
print(random.randint(3, 9))

# random.choice():  The choice() method returns a randomly selected element from the specified sequence.
# The squence can be string, a range, a list,a tuple  or any other kind of sequnce.
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist)) 

# random.shuffle(): The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

