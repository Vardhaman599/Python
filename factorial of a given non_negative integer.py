#Create a program that calculates the factorial of a given non-negative integer.
num = int(input("Enter a non-negative integer:"))
factorial=1
if num<0:
    print("Factorial is undefined for negative numbers.")
elif num ==0:
    print("Factorial of  0 is 1")
else:
    i=1
    while i <= num:
        factorial *=i
        i+=1
    print(f"Factorial of {num} is {factorial}")
3
