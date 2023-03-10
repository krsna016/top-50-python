"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to check if a string contains any special character
"""

string = input("Enter the string : ")
not_special = [chr(i) for i in range(48,59)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + ["_"," "]
for i in string:
    if i not in not_special:
        print("This string contains an special character.")
                