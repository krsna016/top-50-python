"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Ways to remove i'th character from string in Python
"""

string = input("Enter the string : ")
ith = int(input("Enter the ith index : "))
string = string.replace(string[ith],"") # First way
string = string[:ith] + string[ith+1:]  # Second way
print(string)