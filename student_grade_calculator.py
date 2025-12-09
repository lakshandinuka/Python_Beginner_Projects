# Create function to calculate total
def calculate_total(marks):
    return sum(marks.values())

# Create function to calculate average


def calculate_average(total_marks, num_subjects):
    return total_marks / num_subjects

# Create function to determine grade


def determine_grade(average_marks):
    if average_marks >= 85:
        return 'A'
    elif average_marks >= 75:
        return 'B'
    elif average_marks >= 65:
        return 'C'
    elif average_marks >= 50:
        return 'D'
    else:
        return 'F'


# Calculate student grades
print("---- Student Grade Calculator ----")
student = {}
student["name"] = input("Enter Student Name: ")
student["subjects"] = ["Math", "Science", "English"]
student["marks"] = {}

for subject in student["subjects"]:
    marks = int(input(f"Enter marks for {subject}: "))
    student["marks"][subject] = marks

total_marks = calculate_total(student["marks"])
average_marks = calculate_average(total_marks, len(student["subjects"]))
grade = determine_grade(average_marks)

# Print results
print(
    f"Student Name: {student['name']} \nTotal Marks: {total_marks} \nAverage Marks: {average_marks} \nGrade: {grade}")
