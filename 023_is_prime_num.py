"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to check whether a number is Prime number or not
"""

num = int(input("Enter the number : "))
flag = 1
for i in range(2,num):
    if num % i == 0:
        flag = 0
        break
if flag == 1:
    print("Number is prime.")
else:
    print("Number is not prime.")
                