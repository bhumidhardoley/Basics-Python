n = int(input("Enter the numbers of operations: "))
minNumber = 0
for i in range(0,n):
    current_input = int(input("Enter the number: "))
    if i == 0:
        temp = current_input
        minNumber = current_input
    temp = current_input
    if minNumber > temp:
        minNumber = temp
print(f"{minNumber} is minimum")