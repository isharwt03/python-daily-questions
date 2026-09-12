# Day 4 — 10 Questions (Intermediate Level)
# Topics: Loops, Lists, Functions, String Manipulation, and Data Structures

# 1. Take a number and print the multiplication table up to 10.
print("Multiplication Table")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# 2. Take a number and find the sum of all digits.
print("\n Question 2: Sum of Digits ")
num = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(abs(num)))
print(f"Sum of digits: {digit_sum}")


# 3. Take a list of numbers and find the maximum and minimum.
print("\n Question 3: Max and Min from List ")
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")


# 4. Check if a number is a palindrome.
print("\n Question 4: Palindrome Check ")
num = input("Enter a number or string: ")
if num == num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")


# 5. Count the frequency of each character in a string.
print("\n Question 5: Character Frequency ")
text = input("Enter a string: ").lower()
char_freq = {}
for char in text:
    if char != ' ':
        char_freq[char] = char_freq.get(char, 0) + 1
print(f"Character frequency: {char_freq}")


# 6. Reverse a list without using built-in reverse methods.
print("\ Question 6: Reverse a List ")
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
reversed_list = []
for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])
print(f"Reversed list: {reversed_list}")


# 7. Create a function that checks if a number is prime.
print("\n Question 7: Prime Number Check ")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# 8. Take a string and count vowels and consonants.
print("\n Question 8: Vowels and Consonants ")
text = input("Enter a string: ").lower()
vowels = 'aeiou'
vowel_count = sum(1 for char in text if char in vowels and char.isalpha())
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")


# 9. Find common elements between two lists.
print("\n Question 9: Common Elements ")
list1 = list(map(int, input("Enter first list (space-separated): ").split()))
list2 = list(map(int, input("Enter second list (space-separated): ").split()))
common = list(set(list1) & set(list2))
print(f"Common elements: {sorted(common)}")


# 10. Create a function to calculate factorial of a number.
print("\n Question 10: Factorial Calculation ")
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")
