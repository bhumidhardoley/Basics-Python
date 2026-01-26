nRange = int(input("Enter the range(included): "))
sum = 0 

for i in range(1,nRange+1):
    sum = sum + i
print(f"Sum  of {nRange} numbers is {sum}")



numbers = int(input("How many numbers you want to add: "))
num_sum = 0

for i in range(0,numbers):
    current_num = int(input("Add Num: "))
    num_sum = current_num + num_sum

print(f"Total : {num_sum}")