"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to find HCF (GCD) of two numbers
"""

fac_1 = []
fac_2 = []
common_fac = []
num_1 = int(input("Enter first num : "))
num_2 = int(input("Enter second num : "))
for i in range(1,num_1+1):
    if num_1%i == 0:
        fac_1.append(i)
for i in range(1,num_2+1):
    if num_2%i == 0:
        fac_2.append(i)
for i in fac_2:
    if i in fac_1:
        common_fac.append(i)
print(f"The GCD/HCF of the two numbers {num_1} and {num_2} are : {max(common_fac)}")


