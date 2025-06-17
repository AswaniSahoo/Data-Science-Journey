import csv

# write to csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Roll No", "Marks"])
    writer.writerow(["Rahul", "12A", "40"])
    writer.writerow(["Rohit", "12C", "43"])
    writer.writerow(["Aman", "12E", "46"])
    
    
# Read from CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)