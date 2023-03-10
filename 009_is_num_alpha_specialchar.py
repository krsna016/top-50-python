"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to input any character and check whether it is alphabet, digit or special character
"""

input_1 = input("Enter the character : ")
nums = [chr(i) for i in range(48,58)] 
alphas = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]
if input_1 in nums:
    print("It's a number.")
elif input_1 in alphas:
    print("It's an alphabet.")
else:
    print("It's special character.")