"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to count the Number of matching characters in a pair of string
"""

string = input("Enter the string : ")
dict_1 = dict.fromkeys((i for i in string),0)
for i in string:
    dict_1[i] += 1
for k,v in dict_1.items():
    print(f"{k} comes {v} times.")