"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to check whether a number is palindrome or not
"""

num = input("Enter the number : ")
if num == num[::-1]:
    print("It's palindromic.")
else:
    print("Not a palindrome.")   