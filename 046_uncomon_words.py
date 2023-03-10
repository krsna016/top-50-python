"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to find uncommon words from two Strings
"""

str_1 = input("String 1 : ").lower().split()
str_2 = input("String 2 : ").lower().split()
a = set(str_1).difference(str_2)
b = set(str_2).difference(str_1)
print(f"The uncommon words are : {list(a) + list(b)}")





