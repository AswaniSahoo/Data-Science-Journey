def sumation(n): #recurssive condition with 
    if(n==1): #Base condition
        return 1
    return sumation(n-1)+ n

print(sumation(4))