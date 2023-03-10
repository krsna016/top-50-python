"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Find all duplicate characters in string
"""

string = input("Enter the string : ").split()
rep = []
for i in string:
    if string.count(i) > 1 and i not in rep:
        rep.append(i)
print("The repetative words in the string are : ")
for i,j in enumerate(rep):
    print(f"{i+1}.", j)