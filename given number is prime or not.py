#Write a program that checks if a given number is prime.

num=int(input("enter a number:"))

if num<2:
    print("Not prime")
else:
    is_prime = True
    for i in range (2, int(num**0.5)+1):
        if num % i ==0:
            is_prime= False
            break
        if is_prime:
            print("Prime")
        else:
            print("Not prime")
