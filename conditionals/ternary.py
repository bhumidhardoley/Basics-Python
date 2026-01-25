a = 2 
b = 330

print(f"{b} is bigger") if b>a else print(f"{a} is greater than {b}")

# We can also assign values using if and else

bigger = a if a>b else b

print("The bigger number is:",bigger)

name = input("Enter your name: ")
username = name if name else "Guest"
print("welcome",username)


# Ternary operators should be used only when the conditions are simple