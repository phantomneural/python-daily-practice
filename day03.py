
# ==========================================
# DAY 3 - PYTHON LOOPS
# Topics: for, while, range, break, continue
#        nested loops and problem solving
# ==========================================


# Challenge 1: Print numbers from 1 to 50

print("Challenge 1: Numbers from 1 to 50")

for i in range(1, 51):
    print(i)


# Challenge 2: Multiplication Table

print("\nChallenge 2: Multiplication Table")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "*", i, "=", result)


# Challenge 3: Sum of Even Numbers

print("\nChallenge 3: Sum of Even Numbers")

num = int(input("Enter the number: "))
total = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        total = total + i

print("Sum of even numbers:", total)


# Challenge 4: Factorial of a Number

print("\nChallenge 4: Factorial")

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)


# Challenge 5: Prime Number Checker

print("\nChallenge 5: Prime Number Checker")

num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")


# Challenge 6: Pattern Printing

print("\nChallenge 6: Pattern Printing")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


print("\nDay 3 Python practice completed!")
