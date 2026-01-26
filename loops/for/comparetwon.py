import math

n = int(input("Enter range for each set: "))

firstHalf =0
secondHalf =0

for i in range(0,n):
    current_input = int(input("Enter the number: "))
    firstHalf = current_input + firstHalf


print("SECOND HALF")
for i in range(n,2*n):
    current_input = int(input("Enter the number: "))
    secondHalf = current_input+secondHalf

if firstHalf == secondHalf:
    print(f"Both the sum are equal : {firstHalf}")
elif firstHalf != secondHalf:
    print("The difference is :",math.fabs(firstHalf-secondHalf))

# .fabs() method returns absolute value 