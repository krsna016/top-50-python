"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to find LCM of two numbers
"""

def prime_num(num=10):
    n_p = []
    for i in range(3,num+1):
        for j in range(2,(i//2)+1):
            if i % j == 0:
                n_p.append(i)
                break
    p = [i for i in range(2,num+1) if i not in n_p]
    return p

range_p = input("Enter the range of primes (otherwise leave empty) : ")
if range_p:
    search = prime_num(int(range_p))
else:
    search = prime_num()
num_1 = int(input("Enter first num : "))
num_2 = int(input("Enter second num : "))
lcm = 1
while (num_1 != 1 or num_2 != 1):
    for i in search:
        if num_1%i == 0 or num_2%i == 0:
            lcm *= i
            if num_1%i == 0:
                num_1 = num_1//i
            if num_2%i == 0:
                num_2 = num_2//i
            break
print(f"The LCM of the number are : {lcm}")