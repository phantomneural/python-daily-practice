
# ============================================================
# DAY 5 - PYTHON FUNCTIONS
# Topics:
# Function Definition, Parameters, Arguments, Return,
# Default Arguments, Variable Scope, Problem Solving
# ============================================================


# Challenge 1: Basic Function
print("\n--- Challenge 1: Welcome Function ---")

def welcome():
    print("Welcome to Day 5 of Python Learning!")

welcome()


# Challenge 2: Addition Function
print("\n--- Challenge 2: Addition ---")

def add(a, b):
    result = a + b
    return result

print("Addition:", add(10, 20))
print("Addition:", add(5, 15))


# Challenge 3: Even or Odd Function
print("\n--- Challenge 3: Even or Odd ---")

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(10))
print(check_even(7))
print(check_even(24))


# Challenge 4: Factorial Function
print("\n--- Challenge 4: Factorial ---")

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

number = int(input("Enter a number for factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(number))


# Challenge 5: Prime Number Function
print("\n--- Challenge 5: Prime Number Checker ---")

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

num = int(input("Enter a number to check prime: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")


# Challenge 6: Calculator Function
print("\n--- Challenge 6: Calculator ---")

def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    else:
        return "Invalid operator"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, operator)

print("Result:", result)


# Extra Practice: Default Arguments
print("\n--- Default Arguments ---")

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Python Learner")


# Extra Practice: Global Variable
print("\n--- Global Variable ---")

course = "Python Programming"

def show_course():
    print("Current Course:", course)

show_course()


# Mini Project: Student Marks Calculator
print("\n--- MINI PROJECT: STUDENT MARKS CALCULATOR ---")


# Function 1: Get marks
def get_marks():

    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    return mark1, mark2, mark3


# Function 2: Calculate total
def calculate_total(a, b, c):
    return a + b + c


# Function 3: Calculate average
def calculate_average(total):
    return total / 3


# Function 4: Determine grade
def get_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


# Function 5: Display result
def display_result(total, average, grade):

    print("\n========== STUDENT RESULT ==========")

    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

    print("====================================")


# Main Program
marks = get_marks()

total = calculate_total(*marks)

average = calculate_average(total)

grade = get_grade(average)

display_result(total, average, grade)


print("\nDay 5 Python Practice Completed!")
