"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to check whether a number is Armstrong number or not
"""
                
num = input("Enter the number : ")
store = 0
for i in num:
    store += int(i)**len(num)
if store == int(num):
    print("It's armstrong number.")
else:
    print("It's not an armstrong number.")

