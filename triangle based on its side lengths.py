#Create a program that determines the type of a given triangle based on its side lengths.
a= float(input("enter the length of side A:"))
b=float(input("enter the length of side B:"))
c=float(input("enter the lenth of side C:"))
if a ==b==c:
    print("Equilateral triangle ")
elif a ==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene Triangle")
    
