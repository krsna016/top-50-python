"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to check whether the string is Symmetrical or Palindrome
"""

string = input("Enter the string : ")
str_len = len(string)
if string == string[::-1]:
    print("It's palindrome")
else:
    if string[:str_len//2] == string[str_len//2:]:
        print("It's symmetrical string")