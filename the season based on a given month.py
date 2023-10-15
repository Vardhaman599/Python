#Write a program that determines the season based on a given month
Month= input("enter a month:")

if Month in ["Novmber","December","January","February"]:
    print("Winter")
elif Month in ["march","April","May","June"]:
    print("Summer")
elif Month in ["July","August","September","October"]:
    print("Rainy")
else:
    print("Invalid month")
