# Python program to sum of an array

arr = []
inputValue = int(input("Enter Number of Values: "))

for i in range(0, inputValue):
    arrValue = int(input("\nEnter Array Value: "))
    arr.append(arrValue)

summation = 0

for j in range(0, len(arr)):
    summation = summation + arr[j]

print("\n\nThe Array is: ", arr)
print("\nSum of all the elements of the array: " + str(summation))
