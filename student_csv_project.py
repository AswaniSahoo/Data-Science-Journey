import csv

# Function to save data to CSV
def save_to_csv(data):
    with open("students_day1.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Function to calculate average from CSV

def calculate_csv_average():
    total_marks = 0
    count = 0
    with open("students_day1.csv","r") as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        for row in reader:
            total_marks += int(row[2])
            count += 1
    return total_marks / count if count > 0 else 0

with open("students_day1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Roll No", "Marks"])

for i in range(3):
    name = input("Enter student name: ")
    roll_no = int(input("Enter Roll no: "))
    marks = int(input("Enter Marks: "))
    save_to_csv([name,roll_no,marks])
    
avg = calculate_csv_average()
print(f"Average marks of students: {avg}")