"""
Student name        : Anurag Pareek
University roll no. : 2215000322
Contact             : anurag020416@gmail.com
Perpose             : Write a Python program to find all prime factors of a number
"""
                
num = int(input("Enter the number : "))
n_prime = []
for i in range(3,num+1):
    for j in range(2,(i//2)+1):
        if i%j == 0:
            n_prime.append(i)
            break
prime = [i for i in range(2,num) if i not in n_prime]
print(f"The sum of prime numbers are : {sum(prime)}")