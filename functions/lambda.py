# Lamda function in python are small anonymous functions which don't have any defined names: we can define lambda funciton using lmbda keyword

def add(a,b):
    return a+b

sum = lambda a, b: a+b  # It returns the value of the right side of the :
# Syntax:  lambda argument : expression

print(f"Using normal function additin of 1 and 2 :{add(1,2)}")
print(f"Using lamda function addition of 1 and 2 :{sum(1,2)}")


value = lambda a: 'Even' if a %2 ==0 else 'Odd'
check = int(input("Enter a number: "))
print(f'The number is: {value(check)}')