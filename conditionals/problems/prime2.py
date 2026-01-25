import math

number = int(input("Enter the number: "))

if number <= 1:
    print(f"{number} is not Prime number")
else:
    for i in range(2,math.isqrt(number)+1):
        if number % i == 0 :
            print(f"{number} is not prime number")
            break
    else: 
        print(f"{number} is a prime number")