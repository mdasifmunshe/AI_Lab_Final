# Python program to read a file word by word

with open('taskFive.txt', 'r') as file:
    for line in file:
        for word in line.split():
            print(word)
