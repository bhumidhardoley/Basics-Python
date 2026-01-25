# elif allows us to check for multiple true conditions

print("Testing conditions")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a>b:
    print(f"{a} is greater than {b}")
elif b>a: 
    print(f"{b} is greater than {a}")
elif a==b:
    print(f"{a} is equal to {b}")
else:
    print("No conditions are met")
