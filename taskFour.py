# Python program to reverse the words of a string

inputValue = input("Enter The Words: ")

ans = inputValue.split()[::-1]
arr = []
for i in ans:
    arr.append(i)

print("\n\nOriginal Word: " + inputValue)
print("Reversed Word: "+" ".join(arr))
