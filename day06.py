
# ============================================================
# DAY 6 - PYTHON STRINGS
#
# Topics:
# String Indexing, Slicing, Methods, Formatting,
# Immutability and String Problem Solving
#
# Challenges:
# 1. Reverse a String
# 2. Palindrome Checker
# 3. Vowel Counter
# 4. Character Frequency
# 5. Word Counter
# 6. Password Validator
#
# Mini Project: Text Analyzer
# ============================================================


# Challenge 1: Reverse a String
print("\n--- Challenge 1: Reverse a String ---")

word = input("Enter a word: ")

reverse = word[::-1]

print("Original word:", word)
print("Reversed word:", reverse)


# Challenge 2: Palindrome Checker
print("\n--- Challenge 2: Palindrome Checker ---")

word = input("Enter a word: ")

reverse = word[::-1]

if word.lower() == reverse.lower():
    print("Palindrome")
else:
    print("Not a Palindrome")


# Challenge 3: Vowel Counter
print("\n--- Challenge 3: Vowel Counter ---")

text = input("Enter a sentence: ")

vowels = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1

print("Total vowels:", vowels)


# Challenge 4: Character Frequency
print("\n--- Challenge 4: Character Frequency ---")

text = input("Enter a string: ")
character = input("Enter character to count: ")

count = 0

for char in text:
    if char.lower() == character.lower():
        count += 1

print("Character frequency:", count)


# Challenge 5: Word Counter
print("\n--- Challenge 5: Word Counter ---")

sentence = input("Enter a sentence: ")

words = sentence.split()

count = len(words)

print("Total words:", count)


# Challenge 6: Password Validator
print("\n--- Challenge 6: Password Validator ---")

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    else:
        has_special = True


if (len(password) >= 8 and
    has_upper and
    has_lower and
    has_digit and
    has_special):

    print("Strong Password")

else:
    print("Weak Password")

    if len(password) < 8:
        print("Password must contain at least 8 characters")

    if not has_upper:
        print("Add at least one uppercase letter")

    if not has_lower:
        print("Add at least one lowercase letter")

    if not has_digit:
        print("Add at least one digit")

    if not has_special:
        print("Add at least one special character")


# ============================================================
# MINI PROJECT: TEXT ANALYZER
# ============================================================

print("\n--- MINI PROJECT: TEXT ANALYZER ---")

text = input("Enter a sentence for analysis: ")


# 1. Total characters
characters = len(text)


# 2. Total words
words = text.split()
word_count = len(words)


# 3. Count vowels
vowels = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1


# 4. Count consonants
consonants = 0

for char in text.lower():
    if char.isalpha() and char not in "aeiou":
        consonants += 1


# 5. Count digits
digits = 0

for char in text:
    if char.isdigit():
        digits += 1


# 6. Count spaces
spaces = 0

for char in text:
    if char == " ":
        spaces += 1


# 7. Reverse sentence
reverse = text[::-1]


# 8. Display results
print("\n========== TEXT ANALYZER ==========")

print("Original Text:", text)
print("Total Characters:", characters)
print("Total Words:", word_count)
print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
print("Total Digits:", digits)
print("Total Spaces:", spaces)
print("Reversed Sentence:", reverse)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

print("===================================")


print("\nDay 6 Python Practice Completed!")
