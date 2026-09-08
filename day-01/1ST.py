# 🐍 Day 1 — Your 10 Questions

# 1. Take two numbers and print their sum.
print("=" * 50)
print("Question 1: Sum of Two Numbers")
print("=" * 50)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum_result = a + b
print(f"The sum of {a} and {b} is: {sum_result}")


# 2. Take two numbers and print their difference.
print("\n" + "=" * 50)
print("Question 2: Difference of Two Numbers")
print("=" * 50)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

diff = a - b
print(f"The difference of {a} and {b} is: {diff}")


# 3. Take two numbers and print their multiplication.
print("\n" + "=" * 50)
print("Question 3: Multiplication of Two Numbers")
print("=" * 50)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

product = a * b
print(f"The product of {a} and {b} is: {product}")


# 4. Take two numbers and print their division.
print("\n" + "=" * 50)
print("Question 4: Division of Two Numbers")
print("=" * 50)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b == 0:
    print("Error: Cannot divide by zero!")
else:
    division = a / b
    print(f"The division of {a} by {b} is: {division}")


# 5. Take a number and check whether it is even or odd.
print("\n" + "=" * 50)
print("Question 5: Check Even or Odd")
print("=" * 50)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# 6. Take a person's age and check whether they are 18 or older.
print("\n" + "=" * 50)
print("Question 6: Check if Adult (18+)")
print("=" * 50)

age = int(input("Enter your age: "))

if age >= 18:
    print(f"You are {age} years old. You are an adult!")
else:
    print(f"You are {age} years old. You are a minor.")


# 7. Take three numbers and find the largest.
print("\n" + "=" * 50)
print("Question 7: Find Largest of Three Numbers")
print("=" * 50)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = max(num1, num2, num3)
print(f"The largest among {num1}, {num2}, and {num3} is: {largest}")


# 8. Take a number and calculate its square and cube.
print("\n" + "=" * 50)
print("Question 8: Calculate Square and Cube")
print("=" * 50)

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print(f"Square of {num} is: {square}")
print(f"Cube of {num} is: {cube}")


# 9. Take a student's marks and print their percentage for 5 subjects.
print("\n" + "=" * 50)
print("Question 9: Calculate Student's Percentage")
print("=" * 50)

subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))
subject4 = int(input("Enter marks for Subject 4: "))
subject5 = int(input("Enter marks for Subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

print(f"\nTotal Marks: {total_marks}/500")
print(f"Percentage: {percentage}%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")


# 10. Create a simple calculator that takes two numbers and an operator (+, -, *, /) and performs the operation.
print("\n" + "=" * 50)
print("Question 10: Simple Calculator")
print("=" * 50)

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operator! Please use +, -, *, or /")

print("\n" + "=" * 50)
print("✅ All 10 Questions Completed!")
print("=" * 50)
