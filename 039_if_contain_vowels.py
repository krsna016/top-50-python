"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to accept the strings which contains all vowels
"""

string = input("Enter the string : ").lower()
flag = 1
vowels = ["a","e","i","o","u"]
for i in vowels:
    if i not in string:
        flag = 0
        break
if flag == 1:
    print(f"This string follows the criteria :\n{string}")
