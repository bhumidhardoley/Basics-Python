n = int(input("Enter a number (range) : "))

even_sum = 0
odd_sum = 0

for i in range(0,n):
    current_input = int(input("Enter a number: "))
    if current_input % 2 == 0:
        even_sum = even_sum + current_input
    else:
        odd_sum = odd_sum + current_input

print(f"Even: {even_sum} and Odd: {odd_sum}")