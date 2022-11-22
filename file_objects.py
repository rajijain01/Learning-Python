#file objects: open a file 
# test.txt is in same file directory otherwisse youto type the full path of the file.
# 'r' is for read only 
#Explicitely we have to close a file at the end

f = open('test.txt', 'r')

print(f.name)

f.close()

#open a file using the context manager
# here the file is automatically close we dont have to close the file
#f.read(): read the whole file
#f.readlines(): read all the lines as a diffrent element
#f.readline(): read 1st line from the file

with open('test.txt', 'r') as f:
#     pass
# print(f.mode)        
    f_contents = f.read()
    print(f_contents)

# read  2 lines
with open('test.txt', 'r') as f:
     f_contents = f.readline()
     print(f_contents, end='')

     f_contents = f.readline()
     print(f_contents, end='')

# for efficient way to read file without compromising memory
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

#if we want to read exact text in the file
with open('test.txt', 'r') as f:
    f_contents = f.read(100) # reads staring 100 charactersof the file
    print(f_contents, end='')

#if we dont want ot hard code size to read then can make an variable size_to_read
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*') # it will pause at every 10 character
        f_contents = f.read(size_to_read)

# f.tell method tellls you current position of the character in the file

#f.seek() method
with open('test.txt','r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0) #seek(0) is used to start from the beginning of loaction in the file

    f_contents = f.read(size_to_read)
    print(f_contents)

#writing to files
#to write we use "w", be carefull to use the 'w' as it will over-write the file.
#if we dont want to over-write file then use 'a' as append
with open('test2.txt', 'w') as f:
     f.write('Test')
     f.write('Test') #writes test 2 times in test2.txt

#we can use seek(0) to get back to position to beginning of the file,
#here seek(0) overwrote the first one character,

with open('test2.txt', 'w') as f:
     f.write('Test')
     f.seek(0)
     f.write('Test')

#In below example with seek(0) it will not over-write the whole word instead it overwrite only 1st letter of the word 'Rest'
with open('test2.txt', 'w') as f:
     f.write('Test')
     f.seek(0)
     f.write('R')


# Reaad and write on multiple files at the same time
#rf as we read from file in order to write our copy
#wf to write a content to our copy

with open('test3.txt','r' ) as rf:
    with open('test_copy.txt','w' ) as wf:
        for line in rf:
            wf.write(line)


#chunk size 4096 : To read the chunk of the data from original copy


