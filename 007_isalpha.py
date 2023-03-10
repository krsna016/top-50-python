"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to check whether a character is alphabet or not
"""

input_1 = input("Enter the character : ")
alphas = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
if input_1 in alphas:
    print(f"{input_1} is an Alphabet")
else:
    print(f"{input_1} is not an Alphabet")