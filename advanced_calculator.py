import math
print("Created by Jahnavi")
num = float(input("Enter a number: "))

print("1. Square Root")
print("2. Square")

choice = input("Choose (1/2): ")

if choice == "1":
    print("Result:", math.sqrt(num))
elif choice == "2":
    print("Result:", num ** 2)
else:
    print("Invalid choice")
