"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to swap two numbers using bitwise operator
"""

num1,num2 = list(map(int,input("Enter two numbers : (space sep) ").split()))
print()
print("First number is (before swapping) - ",num1)
print("second number is (before swapping) - ",num2)
temp = num1^num2
num1 = temp^num1
num2 = temp^num2
print()
print("First number is (after swapping) - ",num1)
print("second number is (after swapping) - ",num2)

