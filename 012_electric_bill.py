"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to input electricity unit charges and calculate total electricity
                      bill according to the given condition: 
                      For first 50 units Rs. 0.50/unit
                      For next 100 units Rs. 0.75/unit
                      For next 100 units Rs. 1.20/unit
                      For unit above 250 Rs. 1.50/unit, An additional surcharge of 20% is added to the bill
"""

import pyinputplus as ps
unit_ch = ps.inputNum(prompt="Enter a unit charge : ")
charge = 0
total_ch = 0
if unit_ch <= 50 and unit_ch >= 0:
    charge = 0.50
elif unit_ch <= 150 and unit_ch > 50:
    charge = 0.75
elif unit_ch <= 250 and unit_ch > 150:
    charge = 1.20
elif unit_ch > 250:
    charge = 1.50

if unit_ch > 250:
    total_ch = unit_ch*charge + ((20/100)*(unit_ch*charge))
else:
    total_ch = unit_ch * charge
print(f"Total electric bill is : {total_ch}")

