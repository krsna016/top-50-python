"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to find all factors of a number
"""

num = int(input("Enter the number : "))
factors = ""
for i in range(1,num+1):
    if num % i == 0:
        factors += (str(i)+ " ")
print("The factors are :",factors)
