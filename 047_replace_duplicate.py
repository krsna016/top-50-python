"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to replace duplicate occurrence in string
"""

string = input().split()
rep = []
for i in string:
    if string.count(i) > 1 and i not in rep:
        rep.append(i)
rep_dict = dict.fromkeys(rep," ")
for i in rep:
    print(f"Enter the alternative string for the repetative word -> {i}")
    enter = input("Enter the string : \n")
    rep_dict[i] = enter
for i in range(len(string)):
    if string[i] in rep:
        string[i] = rep_dict[string[i]]
print(" ".join(string))
