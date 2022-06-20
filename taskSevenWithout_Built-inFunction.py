# Python program to get number of characters, white space, words and lines in a file
# Without using any built-in function of Python
# Don't forget to get the 'taskSeven.txt' file

# Function to count number
# of characters, words, spaces
# and lines in a file
def counter(fname):
    # variable to store total word count
    num_words = 0

    # variable to store total line count
    num_lines = 0

    # variable to store total character count
    num_charc = 0

    # variable to store total space count
    num_spaces = 0

    # opening file using with() method
    # so that file gets closed
    # after completion of work
    with open(fname, 'r') as f:

        # loop to iterate file
        # line by line
        for line in f:

            # incrementing value of
            # num_lines with each
            # iteration of loop to
            # store total line count
            num_lines += 1

            # declaring a variable word
            # and assigning its value as Y
            # because every file is
            # supposed to start with
            # a word or a character
            word = 'Y'

            # loop to iterate every
            # line letter by letter
            for letter in line:

                # condition to check
                # that the encountered character
                # is not white space and a word
                if letter != ' ' and word == 'Y':

                    # incrementing the word
                    # count by 1
                    num_words += 1

                    # assigning value N to
                    # variable word because until
                    # space will not encounter
                    # a word can not be completed
                    word = 'N'

                # condition to check
                # that the encountered character
                # is a white space
                elif letter == ' ':

                    # incrementing the space
                    # count by 1
                    num_spaces += 1

                    # assigning value Y to
                    # variable word because after
                    # white space a word
                    # is supposed to occur
                    word = 'Y'

                # loop to iterate every
                # letter character by
                # character
                for i in letter:

                    # condition to check
                    # that the encountered character
                    # is not white space and not
                    # a newline character
                    if i != " " and i != "\n":
                        # incrementing character
                        # count by 1
                        num_charc += 1

    # printing total word count
    print("Number of words in text file: ", num_words)

    # printing total line count
    print("Number of lines in text file: ", num_lines)

    # printing total character count
    print('Number of characters in text file: ', num_charc)

    # printing total space count
    print('Number of spaces in text file: ', num_spaces)


# Driver Code:
if __name__ == '__main__':
    fname = 'taskSeven.txt'
    try:
        counter(fname)
    except FileNotFoundError:
        print('File not found')
