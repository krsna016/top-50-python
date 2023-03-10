"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to convert snake case to pascal case
"""

string = input("Enter in snake_case : ").split("_")
for i in range(len(string)):
    string[i] = string[i].title()
string = "".join(string)
print(string)