#Os module: allows to interact with underlying operating system in order to navigate file systems.
#file information and lookup and environmental variables.
#we can move files around
#its an in-built module

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