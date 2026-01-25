a = int(input("Enter the first number: "))
b = int(input("Enter the seconde number: "))
c = int(input("Enter the third number: "))

if a>b and a>c:
    print(f"{a} is greatest")
elif b>c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")