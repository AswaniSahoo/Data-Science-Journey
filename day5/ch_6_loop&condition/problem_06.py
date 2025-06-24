namelist = ["Harry","Rohan","Subham","Aswani","Rahul" ]
name = str(input("Enter Your name: "))
if(name.lower() in namelist):
    print("Your Name is present in the list")
    
else:
    print("Your Name is not in the list")