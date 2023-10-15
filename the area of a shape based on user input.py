# Create a program that calculates the area of a shape based on user input
shape = input ("Enter the shape (Circle,square,triangle):")

if shape =="circle":
    radius =float(input("Enter the radius:"))
    area =3.14159 *radius**2
elif shape=="square":
    side=float(input("Enter the side length:"))
    area =side ** 2
elif shape == "Triangle":
    base = float(input("Enter the base length:"))
    height=float(input("enter the height:"))
    area =0.5*base*height
else:
    print("Invalid shape")
    area = None
if area is not None:
    print(f"The area of the {shape} is {area}")
