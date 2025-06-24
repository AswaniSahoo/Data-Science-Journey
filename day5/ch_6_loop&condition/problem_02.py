print("Enter marks: ")
a1= int(input())
a2= int(input())
a3= int(input())
if(a1>=33 and a2>=33 and a3>=33 and (((a1+a2+a3)/300)*100)>=40):
    print("passed")
else:
    print("fail")