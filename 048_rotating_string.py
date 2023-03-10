"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : String slicing in Python to rotate a string
"""
                
# Rotating string Left and Right by two character:
# Rotating from right:
string = input("Enter the string : ")
rotated_str_r = string[-2:] + string[:-2]
print("Rotated Right :",rotated_str_r)
# Rotating from left:
rotated_str_l = string[2:] + string[:2]
print("Rotated Left :",rotated_str_l)
