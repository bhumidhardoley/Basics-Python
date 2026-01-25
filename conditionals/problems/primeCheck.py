import math

def is_prime(num):

    if num <= 1:
        return False
    else:
        for i in range(2,math.isqrt(num)+1):
            if num % i == 0:
                return False
    return True

number = int(input("Enter the number: "))
print("prime" if is_prime(number) else "Not prime")


    
