"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to check whether a number is Perfect number or not
"""

num = int(input("Enter the number : "))
fac_sum = 0
for i in range(1,num):
    if num % i == 0:
        fac_sum += i
if num == fac_sum:
    print("It's a perfect number")
else:
    print("Not an perfect number")