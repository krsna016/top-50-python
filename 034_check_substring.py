"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to Check if a Substring is Present in a Given String
"""

string = input("Enter the string : ")
sub_string = input("Enter the substring : ")
sub_list = []
for i in range(len(string)+1):
    for j in range(len(string)+1):
        sub_list.append(string[i:j])
if sub_string in sub_list:
    print("Substring is there.")
else:
    print("No such substring.")