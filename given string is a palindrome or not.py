#Write a program that checks if a given string is a palindrome.
T=input("Enter a string")
text=''.join(e for e in T if e.isalnum())
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
