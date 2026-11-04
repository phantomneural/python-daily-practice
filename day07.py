
# ============================================================
# DAY 7 - PYTHON LISTS AND TUPLES
# ============================================================


# Challenge 1: List Basics

print("\n===== CHALLENGE 1: LIST BASICS =====")

numbers = [10, 20, 30, 40, 50]

print("Complete List:", numbers)
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("List Length:", len(numbers))
print("Reversed List:", numbers[::-1])


# ============================================================
# Challenge 2: Sum and Average
# ============================================================

print("\n===== CHALLENGE 2: SUM AND AVERAGE =====")

numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)


# ============================================================
# Challenge 3: Even and Odd Separation
# ============================================================

print("\n===== CHALLENGE 3: EVEN AND ODD SEPARATION =====")

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)


# ============================================================
# Challenge 4: Find Largest and Smallest
# Without using max() or min()
# ============================================================

print("\n===== CHALLENGE 4: LARGEST AND SMALLEST =====")

numbers = [45, 12, 78, 23, 9, 56]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Numbers:", numbers)
print("Largest Number:", largest)
print("Smallest Number:", smallest)


# ============================================================
# Challenge 5: Remove Duplicates
# Preserve original order
# ============================================================

print("\n===== CHALLENGE 5: REMOVE DUPLICATES =====")

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original List:", numbers)
print("Without Duplicates:", unique_numbers)


# ============================================================
# Challenge 6: Find Second Largest Distinct Number
# Without using sort() or sorted()
# ============================================================

print("\n===== CHALLENGE 6: SECOND LARGEST NUMBER =====")

numbers = [10, 25, 8, 45, 30, 45, 20]

largest = None
second_largest = None

for number in numbers:

    if largest is None or number > largest:
        second_largest = largest
        largest = number

    elif number != largest and (
        second_largest is None or number > second_largest
    ):
        second_largest = number

print("Numbers:", numbers)

if second_largest is not None:
    print("Largest Number:", largest)
    print("Second Largest:", second_largest)
else:
    print("Second largest distinct number does not exist.")


# ============================================================
# Challenge 7: List Comprehension
# Squares of even numbers from 1 to 20
# ============================================================

print("\n===== CHALLENGE 7: LIST COMPREHENSION =====")

squares = [
    number ** 2
    for number in range(1, 21)
    if number % 2 == 0
]

print("Squares of Even Numbers:", squares)


# ============================================================
# MINI PROJECT: STUDENT MARKS MANAGER
# ============================================================

print("\n===== STUDENT MARKS MANAGER =====")

marks = []

# Accept marks for five subjects
for i in range(5):

    mark = float(input(f"Enter marks for Subject {i + 1}: "))

    if mark < 0 or mark > 100:
        print("Invalid mark! Enter marks between 0 and 100.")
        break

    marks.append(mark)


# Check whether all five marks were entered
if len(marks) == 5:

    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)

    # Find highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

    # Sort marks in ascending order
    sorted_marks = sorted(marks)

    # Check pass or fail
    passed = True

    for mark in marks:
        if mark < 40:
            passed = False

    # Display student report
    print("\n===== STUDENT MARKS REPORT =====")

    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)
    print("Sorted Marks:", sorted_marks)

    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")


# ============================================================
# TUPLE PRACTICE
# ============================================================

print("\n===== TUPLE PRACTICE =====")

coordinates = (10, 20, 30)

print("Tuple:", coordinates)
print("First Element:", coordinates[0])
print("Last Element:", coordinates[-1])
print("Tuple Length:", len(coordinates))

# Tuple cannot be modified after creation


# ============================================================
# DAY 7 COMPLETED
# ============================================================

print("\n================================")
print("DAY 7 PYTHON PRACTICE COMPLETED!")
print("================================")
