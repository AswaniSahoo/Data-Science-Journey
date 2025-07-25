n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(" " * (n-i),end="")# end="" donot gives a new line otherwise print give by default new line
    print("*" * (2*i-1),end="")
    print("") #here i need a new line so printing blank