#No.1
name = input("Enter your name: ")
date = input("Enter the date: ")

#new method to intoduce variable inside string using f string
print(f"Good Afternoon, {name}")
#No.2
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", f"{name}").replace("<|Date|>",f"{date}"))
#chaning of .replace is used in above string
print(letter)#strings are immutable means it remain unchange 