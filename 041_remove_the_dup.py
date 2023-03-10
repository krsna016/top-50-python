"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Remove all duplicates from a given string in Python
"""

string = input("Enter the string : ")
string = list(string)
for i in string:
    if string.count(i) > 1:
        while i in string:
            string.remove(i)
print(f"The required string is : {''.join(string)}")
                        