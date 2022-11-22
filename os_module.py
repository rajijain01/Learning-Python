#Os module: allows to interact with underlying operating system in order to navigate file systems.
#file information and lookup and environmental variables.
#we can move files around
#its an in-built module


# To check to see if a file exists, the os module needs to be imported and os.path.isfile command is used.for e.g
import os
if os.path.isfile('results.txt')
   writefile = open('results.txt', 'a')
else:
    writefile = open('results.txt', 'w')



import os

#all attributes and methods that we have access within module.
print(dir(os))

#print out current directory
print(os.getcwd())

#navigate to new location on file system,navigate to desktop:
#os.chdir('/mnt/c/Users/samee/Desktop/')

#List directories and files:

print(os.listdir())

#To create a folder on desktop name:'OS-Dem0-2':
#os.makedirs('OS-Demo-2')

#delete folders:
#os.removedirs('OS-Demo-2')

#to get information of file
#print(os.stat('file-name'))

#current date and time:
# import os
# from datetime import datetime

# mod_time = os.stat('file-name').st__mtime
# print(datetime.fromtimestamp(mod_time))

#os.walk() method prints tree directory
for dirpath, dirnames, filenames in os.walk((os.getcwd())):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#envionmental directory
#print(os.environ.get('HOME'))



#SYS MODULE
#The sys module is used to display exception information, error information, and other system information.