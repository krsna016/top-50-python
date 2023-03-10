"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python programs to count maximum frequency character in String
"""

string = input("Enter the string : ")
least_frequent = []
least_frequent_chars = []
for i in string:
    least_frequent.append(string.count(i))
for i in string:
    if string.count(i) == max(least_frequent):
        least_frequent_chars.append(string[string.index(i)])
print("The maximum frequent chars are : ",set(least_frequent_chars))       