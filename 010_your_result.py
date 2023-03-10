"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to input marks of five subjects Physics, Chemistry, Biology,
                      Mathematics and Computer. Calculate percentage and grade according to following:
                      Percentage >= 90% : Grade A
                      Percentage >= 80% : Grade B
                      Percentage >= 70% : Grade C 
                      Percentage >= 60% : Grade D 
                      Percentage >= 40% : Grade E 
                      Percentage <  40% : Grade F
"""

marks_total = sum(list(map(int,input("Enter the marks of 5 subjects (space sep) : ").split(" "))))
percentage = marks_total/5
result = ""
if percentage >= 90 and percentage <= 100:
    result += "A"
elif percentage >= 80 and percentage < 90:
    result += "B"
elif percentage >= 70 and percentage < 80:
    result += "C"
elif percentage >= 60 and percentage < 70:
    result += "D"
elif percentage >= 40 and percentage < 60:
    result += "E"
elif percentage < 40:
    result += "F"
else:
    print("Wrong Input. Enter the valid input.")
print(f"Result : Grade {result}")
