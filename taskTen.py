# Python program to find minimum and maximum k elements in tuple
# Using sorted() + loop

# initializing tuple
test_tup = ()
inputValue = int(input("Enter Number of Values: "))

for i in range(0, inputValue):
    tupValue = input("\nEnter Tuple Value: ")
    test_tup += (tupValue,)

# printing original tuple
print("\n\nThe original tuple is : " + str(test_tup))

# initializing K
K = 2

# Maximum and Minimum K elements in Tuple
# Using sorted() + loop
res = []
test_tup = list(sorted(test_tup))

for idx, val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)

# printing result
print("The extracted values : " + str(res))
