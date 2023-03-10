"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Reverse words in a given String in Python
"""

string = input("Enter the string : ").split(" ")
for i in range(len(string)):
    string[i] = string[i][::-1]
print(" ".join(string))
