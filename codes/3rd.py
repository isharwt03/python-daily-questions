# Day 3 — Your 10 Questions (Strings & Functions)

# 1. Take a string and print its length.
print("printing the length of a string")

str1 = input("Enter a string: ")
print("Length of the string:", len(str1))

# 2. Take a string and convert it to uppercase and lowercase.
print("\n converting string to uppercase and lowercase")

str2 = input("Enter a string: ")
print("Uppercase:", str2.upper())
print("Lowercase:", str2.lower())

# 3. Take a string and check if it contains a specific character.
print("\n checking if string contains a specific character")

str3 = input("Enter a string: ")
char = input("Enter the character to find: ")
if char in str3:
    print(f"The character '{char}' is present in the string")
else:
    print(f"The character '{char}' is not present in the string")

# 4. Take a string and replace a character with another character.
print("\n replacing a character with another character")

str4 = input("Enter a string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
result = str4.replace(old_char, new_char)
print("String after replacement:", result)

# 5. Take a string and split it into a list of words.
print("\nsplitting a string into words")

str5 = input("Enter a string with words separated by spaces: ")
words = str5.split()
print("List of words:", words)

# 6. Create a function to calculate the factorial of a number.
print("\n calculating factorial using a function")

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Enter a number to find factorial: "))
print(f"Factorial of {num} is:", factorial(num))

# 7. Create a function to check if a number is prime.
print("\ nchecking if a number is prime using a function")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num2 = int(input("Enter a number to check if it's prime: "))
if is_prime(num2):
    print(f"{num2} is a prime number")
else:
    print(f"{num2} is not a prime number")

# 8. Create a function that takes multiple parameters and returns their sum.
print("\n summing multiple numbers using a function")

def sum_numbers(*args):
    return sum(args)

num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
total = sum_numbers(*num_list)
print(f"Sum of the numbers: {total}")

# 9. Create a function to check if a string is a palindrome.
print("\n checking if a string is a palindrome using a function")

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

str6 = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(str6):
    print(f"'{str6}' is a palindrome")
else:
    print(f"'{str6}' is not a palindrome")

# 10. Create a function that returns multiple values.
print("\n function returning multiple values")

def get_min_max(numbers):
    return min(numbers), max(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
min_val, max_val = get_min_max(numbers)
print(f"Minimum: {min_val}, Maximum: {max_val}")
