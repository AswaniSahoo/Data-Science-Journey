print('''Here is the infor mation 
      about the multiline statement
      how to print with single print function
      by giving triple single quote .''')


import pyttsx3
engine = pyttsx3.init()
engine.say("hi, i am your personal voice commander.")
engine.runAndWait()


# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 
import os

# Replace 'your_directory_path' with the path of your directory
directory_path = '/movies'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
