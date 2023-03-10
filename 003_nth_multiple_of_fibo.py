"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Python Program for nth multiple of a number in Fibonacci Series
"""

num = int(input("Enter the range : "))
nth = int(input("Enter the nth num for multiples : "))

i = 0
j = 1
fibo = [i,j]
for m in range(num):
    k = i + j
    fibo.append(k)
    i,j = j,k
print(f"The required series are : {list(nth*k for k in fibo)}")
