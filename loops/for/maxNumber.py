nRange = int(input("Enter numbers to compare: "))
temp = 0
max_number = 0 

for i in range(0,nRange):
    current_number = int(input("Enter the number: "))
    temp = current_number
    if temp > max_number:
        max_number = temp
print(f"{max_number} is greatest")
