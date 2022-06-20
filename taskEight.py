# Python program to merge two files into a third file
# Don't forget to get the 'taskEight1.txt' file
# Don't forget to get the 'taskEight2.txt' file
# Don't forget to get the 'taskEight3.txt' file

data = data2 = ""

# Reading data from file1
with open('taskEight1.txt') as fp:
    data = fp.read()

# Reading data from file2
with open('taskEight2.txt') as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

with open('taskEight3.txt', 'w') as fp:
    fp.write(data)
