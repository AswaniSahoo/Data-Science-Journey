a = str(input("Enter your comment: "))
b = ["Make a lot of money","buy now", "subscribe this", "click this"]
spam = False
for i in b:
    if i in a:
        spam = True
        print('spam')
        break
if spam == False:
    print("not spam")