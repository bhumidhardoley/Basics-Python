# and when both conditions neeed to satisfy 

name = "Bhumidhar"
is_student = False

if name and is_student:
    print("Welcome",name,"to dashboard")
else:
    print("You are not a student")

# or operator is needed to combine conditions and only one need to satisfy 

n1 = 2 
n2 = False

if n1 or n2:
    print("Conditions satisfy")

# Not operator is used to indicate negations

a = 2 
b = 3
if not a>b:
    print(f"{b} is greater than {a}")


# Combining multiple operators: 

student = False
age = 24
discount_coupoun = ""

if (age<25 or age>65) and student or discount_coupoun:
    print("Discount applies")
else: 
    print("You are not eligible for any discounts")