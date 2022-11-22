
# Explanation
# To use + operator for string types, compulsory both arguments must be str type, otherwise we will get error.
# print('Congratulations on '+ (int(end)-int(start))+' Years of Service!')
# TypeError: must be str, not int
# print('Congratulations on '+ str(int(end)-int(start))+' Years of Service!')
# print('Congratulations on '+ int(end-start)+' Years of Service!')
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print('Congratulations on '+ str(end-start)+' Years of Service!')
# TypeError: unsu'str'TypeError: unsupported operand type(s) for -: 'str' and 'str'pported operand type(s) for -: 'str' and 



#  In Python, the \ symbol tells Python 'continue this statement on the next line.'
# \n tells Python to  print a new line.
#  \t tells python to insert a tab.
# \\ tells Python to use the \character ; the \ charecter is an escape character


#CONCATENATING symbol is , (comma)
# The symbol to concatenate text and a number within a print statement is a COMMA, not plus sign
#Ther symbol to cancatenate two strings of tet is a plus sign.



#FORMATTED TEXT: To indicate the presence of formatted text, such as variable inside of a sentence, the f synbol is needed.

    start=input('How old were you at the time of joining?')
    end=input('How old are you today?')