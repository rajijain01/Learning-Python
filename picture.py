# workfile = open("picture.txt", "rb")
# workfilecontents = workfile.read()
# print(workfilecontents)
# workfile.close()

with open('picture.png', 'rb') as rf:
    with open('picture1.png', 'wb') as wf:
        for line in rf:
            wf.write(line)