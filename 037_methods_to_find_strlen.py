"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Find length of a string in python (4 ways)
"""

# Method 1:
str_1 = input("Enter the string : ")
print(f"Length of the string is : {len(str_1)}")

# Method 2:
str_2 = input("Enter the string : ")
i = 0
for i in str_2:
    i += 1
print(f"Length of the string is : {i}")

# Method 3:
str_3 = input("Enter the string : ")
i = 0
flag = 1
while flag != 0:
    try:
        str_3[i]
    except IndexError:
        flag = 0
        break
    i += 1
print(f"Lenght of the string is : {i}")

# Method 4:
str_4 = input("Enter the string : ")
value = str_4[-1]
list_val = []
while value in str_4:
    list_val.append(str_4.index(value))
    str_4 = str_4[:str_4.index(value)]+str_4[str_4.index(value)+1:]
print(f"Length of the string is : {list_val[-1]+1}")
