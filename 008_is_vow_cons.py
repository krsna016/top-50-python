"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to input any alphabet and check whether it is vowel or consonant
"""

input_1 = input("Enter the alphabets : ").lower()
vow_cons = ["a","e","i","o","u"]
if input_1 in vow_cons:
    print(f"{input_1} is vowel.")
else:
    print(f"{input_1} is consonant.")