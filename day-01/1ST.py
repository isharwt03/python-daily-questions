# Day 1 — 10 Questions.

import numpy as np 

# 1.Take two numbers and print their sum.
print("sum of two numbers ")
a = int(input ("Enter the first number :"))
b = int(input("Enter the second number:"))

sum = a +b
print ("the sum of two numbers is :",sum)


# 2.Take two numbers and print their difference.
print("difference of two numbers ")
a = int(input ("Enter the first number :"))
b = int(input("Enter the second number:"))

diff = a - b
print ("the difference of two numbers is :",diff)

 
# 3.Take two numbers and print their multiplication.
print("multiplication of two numbers")
a = int(input ("Enter the first number :"))
b = int(input("Enter the second number:"))

multi = a**b
print ("the multiplication of two numbers is :",multi)


# 4.Take two numbers and print their division.
print("division of two numbers")

a = int(input ("Enter the first number :"))
b = int(input("Enter the second number:"))

div = a/b
print ("the division of two numbers is :",div)


# 5.Take a number and check whether it is even or odd.
print("checking whether the number is even or odd")

a = int(input ("Enter the first number :"))
b = int(input("Enter the second number:"))

if a%2==0:
    print("the number is even")
else:
    print("the number is odd")

# 6.Take a person's age and check whether they are 18 or older.
print("checking the age of a person whether they are 18 or older")

a = int(input ("Enter the age of yours according to your governmentdocumentations :"))

if a>=18:
    print("You are eligible to vote ")
else:
    print("You are not eligible to vote under 18 years of age ")

# 7.Take three numbers and find the largest.
print("finding the largest no among 3 numbers ")

a = int(input ("Enter the first number :"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if a>=b and a>=c:
    print("the largest number is :",a)
elif b>=a and b>=c:
    print("the largest number is :",b)
else:
    print("the largest number is :",c)

# 8.Take a number and calculate its square and cube.
print("calculating the square and cube of a number:")

a = int(input ("Enter the number :"))

sq=a**2
cb=a**3

print("the square of the number is :",sq)
print("the cube of the number is :",cb)

# 9.Take a student's marks and print their percentage for 5 subjects.
print("calculating the percentage of a student for 5 subjects")

a = int(input ("Enter the first subject marks :"))
b = int(input ("Enter the second subject marks :"))
c = int(input ("Enter the third subject marks :"))
d = int(input ("Enter the forth subject marks :"))
e = int(input ("Enter the fifth subject marks :"))

marks= a+b+c+d+e
per=(marks/500)*100
print("the percentage of the student is :",per)

# 10.Create a simple calculator that takes two numbers and an operator (+, -, *, /) and performs the operation.
print("simple calculator")

a = int(input ("Enter the first number :"))
b = int(input("Enter the second number:"))

oper = input("Enter the operator (+, -, *, /): ")

if oper =="+":
    result = a+b
    print("the result of addition is :",result)
elif oper =="-":
    result = a-b
    print("the result of subtraction is :",result)
elif oper =="*":
    result = a*b
    print("the result of mutiplication is :",result)
elif oper =="/":
    result = a/b
    print("the result of division is :",result)



