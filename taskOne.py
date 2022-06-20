# Python Program to find the largest number of the array

arr = []
inputValue = int(input("Enter Number of Values: "))

for i in range(0, inputValue):
    arrValue = input("\nEnter array Value: ")
    arr.append(arrValue)

maximum = arr[0]

for j in range(0, len(arr)):
    if arr[j] > maximum:
        maximum = arr[j]

print("\n\nThe Array is: ", arr)
print("\nLargest element present in given array: " + str(maximum))


