"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python program to print even length words in a string
"""
                
string = input("Enter the string : ").split()
for i in string:
    if len(i) % 2 == 0:
        print(i)
    else:
        pass