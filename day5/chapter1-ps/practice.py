# Using Unicode escape sequences
print("\u2764")  # Output: ❤
print("\U0001F600")  # Output: 😀

# Directly typing Unicode characters
print("I love Python ❤")  # Output: I love Python ❤
print("Smiley face 😀")   # Output: Smiley face 😀

# Using chr() function
print(chr(0x2764))  # Output: ❤
print(chr(0x1F600)) # Output: 😀

# Using unicodedata module
import unicodedata

heart = unicodedata.lookup("HEAVY BLACK HEART")
print(heart)  # Output: ❤

smiley = unicodedata.lookup("CRYING FACE")
print(smiley)  # Output: 😀

# Combining characters and formatting
print(f"I love Python {chr(0x2764)}")  # Output: I love Python ❤
print(f"Smiley face {chr(0x1F600)}")   # Output: Smiley face 😀

# Decimal notation
heart_decimal = chr(10084)
print(heart_decimal)  # Output: ❤

# Hexadecimal notation
heart_hex = chr(0x2764)
print(heart_hex)  # Output: ❤

# Both will output the same character
print(heart_decimal == heart_hex)  # Output: True
