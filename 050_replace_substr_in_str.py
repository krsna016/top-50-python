"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Replace all occurrences of a substring in a string
"""

string = input("Enter the string : ")
sub_str = []
for i in range(len(string)+1):
    for j in range(1,len(string)+1):
        if string[i:j] != "":
            sub_str.append(string[i:j])
sub = input("Enter substring and new word to replace with (space sep) resp : ").split()
if sub[0] in sub_str:
    string = string.replace(sub[0],sub[1])
print(string)

