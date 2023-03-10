"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python Program for How to check if a given number is Fibonacci number
"""

from math import sqrt
num = int(input("Enter the number : "))
if num == 0 or num == 1:
    print("Number is in fibonacci series.")
if sqrt(5*(num**2)+4).is_integer() or sqrt(5*(num**2)-4).is_integer():
    print("Number is in fibonacci series.")
else:
    print("Number not in fibonacci series.")