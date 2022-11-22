#The finallly statement always runs when part of a try/except/finally block.
# Thus, the finally statement will print regardless of whether the try or except ppart runs.
#The try and except parts do not both run as part of a try/except/finally block.
# Either the try part works or the except part runs.
#The elses part runsif the try part succeeds. 
#In order to dsiplay an error message when an eerror occurs, the code to run should be in a try block and
#the code to run if there is an error should be in an except block. 

a = 2
b = 0

try:
    print(a/b)

except Exception:
    
    print("you cannot divide number by zero")
print('bye')


a = 5
b = 2
try:
    print(a/b)
except Exception as e:
    print("you cannot divide number by zero", e)
finally:
    print('Finally done')


a = 5
b = 2



try:
    print(a/b)
    k = int(input('Enter a number'))
    print(k) 
except ZeroDivisionError as e:
    print("you cannot divide number by zero", e)
except ValueError as e:
    print("Invalid input")
except Exception as e :
    print('Something went wrong')  

finally:
    print('Finally done')


#example
def f():
   try:
      return 1
   finally :
      return 2
x=f()
print(x)

#example
try:
    print('try')
    print(10/0)
except:
    print('except')
else:
    print('else')
finally:
    print('finally')


#example
import sys
try:
    file_in=open('in.txt','r')
    file_out=open('out.txt', 'w+')
except IOError:
    print('cannot open',file_name)
else:
    i=1
    for line in file_in:
        print(line.rstrip())
        file_out.write(str(i)+':'+line)
        i=i+1
    file_in.close()
    file_out.close()
    



