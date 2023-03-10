"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to calculate product of digits of a number
"""
                
num = input("Enter the num : ")
mul = 1
for i in num:mul *= int(i)
print("The required ans :",mul)