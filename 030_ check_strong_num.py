"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to check whether a number is Strong number or not
"""
                
num = input("Enter the num : ")
sum = 0
mul = 1
for i in num:
    i = int(i)
    for j in range(1,i+1):
        mul *= j
    sum += mul
    mul = 1
if sum == int(num):
    print("It's strong number")
else:
    print("Not a strong number")