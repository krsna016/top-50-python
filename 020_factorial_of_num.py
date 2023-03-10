"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to calculate factorial of a number
"""
                
factorial = 1
for i in range(1,int(input("Enter the num : "))+1):
    factorial *= i
print(f"The factorial is {factorial}")