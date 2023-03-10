"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to input basic salary of an employee and calculate its Gross salary according to following:
                      Basic Salary <= 10000 : HRA = 20%, DA = 80%
                      Basic Salary <= 20000 : HRA = 25%, DA = 90%
                      Basic Salary >  20000 : HRA = 30%, DA = 95%
"""

import pyinputplus as pyip
basic_sal = pyip.inputNum("Enter basic salary : ")
HRA = 0
DA = 0
if basic_sal <= 10000:
    HRA = 20
    DA = 80
elif basic_sal <= 20000 and basic_sal > 10000:
    HRA = 25
    DA = 90
elif basic_sal > 20000:
    HRA = 30
    DA = 95
gross_sal = basic_sal + (basic_sal*(HRA/100) + basic_sal*(DA/100))
print(f"Gross salary is : ₹ {gross_sal}")