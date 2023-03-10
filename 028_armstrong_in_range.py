"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to print all Armstrong numbers between 1 to n
"""
                
num = int(input("Enter the number : "))
print(f"The armstrong numbers in the range 0-{num} are : ")
for i in range(num+1):
    i = str(i)
    len_num = len(i)
    # i = int(i)
    store = 0 
    for k in i: 
        store += (int(k) ** len_num)
    if store == int(i):
        print(i,end=" ")      
print()
