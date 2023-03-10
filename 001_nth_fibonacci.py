"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python Program for n-th Fibonacci number
"""

term = int(input("Enter the term : "))
a,b = 0,1
print(a,b,sep=" ",end=" ")
for i in range(1,term-2+1):
    k = a+b
    print(k,end=" ")
    a,b = b,k
print()