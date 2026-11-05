
# ============================================================
# DAY 08 - PYTHON DICTIONARIES AND SETS
# ============================================================


# ============================================================
# CHALLENGE 1: STUDENT DICTIONARY
# ============================================================

print("\n===== CHALLENGE 1: STUDENT DICTIONARY =====")

student = {
    "name": "Arun",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# CHALLENGE 2: DICTIONARY UPDATE
# ============================================================

print("\n===== CHALLENGE 2: DICTIONARY UPDATE =====")

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 1500,
    "Keyboard": 1000,
    "Mouse": 500
}

# Add a new product
products["Monitor"] = 12000

# Update an existing product price
products["Laptop"] = 55000

# Remove a product
products.pop("Mouse")

print("Updated Product List:")

for product, price in products.items():
    print(product, ":", price)


# ============================================================
# CHALLENGE 3: WORD FREQUENCY COUNTER
# ============================================================

print("\n===== CHALLENGE 3: WORD FREQUENCY =====")

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)


# ============================================================
# CHALLENGE 4: CHARACTER FREQUENCY
# Ignore spaces and uppercase/lowercase differences
# ============================================================

print("\n===== CHALLENGE 4: CHARACTER FREQUENCY =====")

text = input("Enter a string: ")

text = text.lower()

frequency = {}

for char in text:

    if char == " ":
        continue

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nCharacter Frequency:")

for char, count in frequency.items():
    print(char, ":", count)


# ============================================================
# CHALLENGE 5: REMOVE DUPLICATES USING SETS
# ============================================================

print("\n===== CHALLENGE 5: REMOVE DUPLICATES =====")

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique_numbers = set(numbers)

print("Original List:", numbers)
print("Unique Elements:", unique_numbers)


# ============================================================
# CHALLENGE 6: SET OPERATIONS
# ============================================================

print("\n===== CHALLENGE 6: SET OPERATIONS =====")

A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

print("Set A:", A)
print("Set B:", B)

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("A - B:", A - B)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)


# ============================================================
# CHALLENGE 7: FIND COMMON ELEMENTS
# ============================================================

print("\n===== CHALLENGE 7: COMMON ELEMENTS =====")

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common)


# ============================================================
# MINI PROJECT: STUDENT DATABASE MANAGEMENT SYSTEM
# ============================================================

print("\n===== STUDENT DATABASE MANAGEMENT SYSTEM =====")

# Initial student records

students = {
    "Arun": {
        "Python": 85,
        "Maths": 90,
        "English": 80
    },
    "Rahul": {
        "Python": 90,
        "Maths": 88,
        "English": 92
    }
}


# Function to add a student
def add_student():

    name = input("Enter student name: ").strip().title()

    if not name:
        print("Name cannot be empty.")
        return

    if name in students:
        print("Student already exists!")
        return

    marks = {}

    subjects = ["Python", "Maths", "English"]

    for subject in subjects:

        try:
            mark = float(input(f"Enter {subject} marks: "))

            if mark < 0 or mark > 100:
                print("Invalid marks! Enter between 0 and 100.")
                return

            marks[subject] = mark

        except ValueError:
            print("Please enter a valid number.")
            return

    students[name] = marks

    print("Student added successfully!")


# Function to display all students
def display_students():

    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for name, marks in students.items():

        print("\nName:", name)

        for subject, mark in marks.items():
            print(subject, ":", mark)


# Function to search for a student
def search_student():

    name = input("Enter student name to search: ").strip().title()

    if name in students:

        print("\nStudent Found!")
        print("Name:", name)

        for subject, mark in students[name].items():
            print(subject, ":", mark)

    else:
        print("Student not found!")


# Function to calculate student averages
def calculate_averages():

    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT AVERAGES =====")

    for name, marks in students.items():

        average = sum(marks.values()) / len(marks)

        print(name, "Average:", round(average, 2))


# Function to find the topper
def find_topper():

    if not students:
        print("No student records found.")
        return

    topper = None
    highest_average = -1

    for name, marks in students.items():

        average = sum(marks.values()) / len(marks)

        if average > highest_average:
            highest_average = average
            topper = name

    print("\nTopper:", topper)
    print("Average:", round(highest_average, 2))


# Function to delete a student
def delete_student():

    name = input("Enter student name to delete: ").strip().title()

    if name in students:

        del students[name]

        print("Student deleted successfully!")

    else:
        print("Student not found!")


# Main menu

while True:

    print("\n================================")
    print(" STUDENT DATABASE MANAGEMENT")
    print("================================")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Calculate Averages")
    print("5. Find Topper")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_averages()

    elif choice == "5":
        find_topper()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("Thank you for using Student Database!")
        break

    else:
        print("Invalid choice! Try again.")


# ============================================================
# DAY 08 COMPLETED
# ============================================================

print("\n================================")
print("DAY 08 PYTHON PRACTICE COMPLETED!")
print("================================")
