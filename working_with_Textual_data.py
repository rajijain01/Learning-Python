message = "Hello World"
#print statement "Hello world"
print(message)
#print lenght of the message 
print(len(message))
#print letter H as it hold the position zero.
print(message[0])
#print the word Hello starting from zero H till 5th position O.
print(message[0:5])
#print the message into all lower case
print(message.lower())
#prints upper case
print(message.upper())
#prints the number of count of the string
print(message.count("Hello World"))
#print the number of count of character "l" in cstring
print(message.count("l"))
#if we want to replace in the string with the other new word then code is as follows
message = message.replace("World","Universe")
print(message)
#concatenate we can use + sign to join 2 string
greeting = "Hello"
name = "Michael"
message = greeting + ", " + name
print(message)
#