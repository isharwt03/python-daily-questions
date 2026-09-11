# Day 2 — Your 10 Questions (Loops & Lists)
import numpy as np 

# 1. Print numbers from 1 to 10 using a for loop.
print("printing numbers from 1 to 10 using loops")

for i in range (1,11):
    print(i)

# 2. Print the multiplication table of a given number (1 to 10).
print("mutiplication table of a given number")

n= int(input("enter the number:"))
for i in range (1,11):
    print(n*i)

# 3. Take a list of numbers and find the sum of all elements.
print("finding the sum of all elements in a list of numbers")

l1=[1,2,3,4,5]
print("sum of all elements:", sum(l1))

# 4. Take a list of numbers and find the maximum and minimum values.
print("finding the maximum and minimum values in a list of numbers")

list1=[1,2,3,4,5]
print 

# 5. Take a list of numbers and reverse it.
print("reversing a list of numbers")

list1=[1,2,3,4,5]
list1.reverse()
print("the reversed list is :",list1)

# 6. Count how many times a number appears in a list.
print("counting how many times a number appears in a list")

list2=[1,2,3,1,1,2,3,1,1,1,1]
print("the number of times 1 appered in list is :",list2.count(1))

# 7. Create a list of squares of numbers from 1 to 10 using list comprehension.
print("creating a list of squares of numbers from 1 to 10 using list comprehension")

square =[num **2 for num in range (1,11)]
print(square)

# 8. Take a string and print each character on a new line.
print("printing each character of a string on a new line")

str= "isha"
for char in str:
    print(char)

# 9. Take a string and count the number of vowels and consonants.
print("counting the number of vowels and consonants in a string")

str1="qqqq"
v=0
c=0
for i in str1:
    if i in "aeiou":
        v+=1
    else:
        c+=1
print("number of vowels:", v)
print("number of consonants:", c)

# 10. Take a number and check if it's a palindrome using a while loop.
print("checking whether the number is a palindrome or not")

num3=input("enter the number:")
rev=num3[::-1]
if num3==rev:
    print ("the number is a palindrome")
else:
    print("the number is not a palindrome")