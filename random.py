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
