name = "Aswani"
print("Length:", len(name))  # Output: 6

print("Lowercase:", name.lower())  # Output: aswani
print("Uppercase:", name.upper())  # Output: ASWANI
print("Capitalize:", name.capitalize())  # Output: Aswani
print("Title:", name.title())  # Output: Aswani

text = "  hello world  "
print("Strip:", text.strip())  # Output: "hello world"
print("Right Strip:", text.rstrip())  # Output: "  hello world"
print("Left Strip:", text.lstrip())  # Output: "hello world  "

text = "hello world"
print("Find 'world':", text.find("world5"))  # Output: 6
text = "hello world world"
print("Replace 'world' with 'there':", text.replace("world", "there"))  # Output: hello there there

text = "hello world"
words = text.split()
print("Split:", words)  # Output: ['hello', 'world']
print("Join:", " ".join(words))  # Output: hello world

print("Starts with 'hello':", text.startswith("hello"))  # Output: True
print("Ends with 'world':", text.endswith("world"))  # Output: True

print("Is alpha:", "hello".isalpha())  # Output: True
print("Is digit:", "12345".isdigit())  # Output: True
print("Is alnum:", "hello123".isalnum())  # Output: True

print("Swap case:", "Hello World".swapcase())  # Output: hELLO wORLD

text = "hello world, hello universe"
print("Count 'hello':", text.count("hello"))  # Output: 2

number = "42"
print("Zfill:", number.zfill(5))  # Output: 00042

#use of escape sequence 
a ="Harry is agood boy \n but not a bad \"boy\" "
print(a)
