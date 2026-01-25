# In nested If we can combine multiple if statemetns

age = int(input("Enter your age: "))
license = False
if age>18:
    if license: print("You can drive")
    else: print("You need a license")
else: 
    print("You are not eligible")
    