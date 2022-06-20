# Python program to find if a string is palindrome or not

def isPalindrome(word):
    return word == word[::-1]


inputValue = input("Enter The Word: ")
ans = isPalindrome(inputValue)

if ans:
    print("\n\nThe Word \"" + inputValue + "\" is a Palindrome")
else:
    print("\n\nThe Word \"" + inputValue + "\" is not a Palindrome")
