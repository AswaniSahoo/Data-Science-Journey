a = int(input("Enter a number: "))
if(a<2):
    print("Enter greater number than 2.")
for i in range(2,a):
    if(a%i == 0 and a!=2):
        print(f"{a} is not a prime no.")
        break
        
    else:
        print(f"{a} is a prime no. ")
        break