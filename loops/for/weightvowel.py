string = input("Enter a string: ")
string = string.lower().strip()

a = e = i = o = u = 0
Total_weight = 0

for h in string:
    if h == 'a':
        a = a+1
        Total_weight = Total_weight + 1
    elif h == 'e':
        e = e+2
        Total_weight = Total_weight + 2
    elif h == 'i':
        i = i+3
        Total_weight = Total_weight + 3
    elif h == 'o':
        o = o + 4
        Total_weight = Total_weight + 4
    elif h == 'u':
        u = u +5
        Total_weight = Total_weight + 5

print("The weights are :")

print(f"a: {a}",f"e: {e}",f"i: {i}",f"o: {o}",f"u: {u}")
print(f"Total weight: {Total_weight}")