# I would say when there are multiple options using if is not that good in that case we can use match

print("Day finder")

day_no = int(input("Enter the date: "))

match day_no:
    case 1:
        print("This is sunday")
    case 2:
        print("This is monday")
    case 3:
        print("This is Tuesday")
    case 4:
        print("This is wednesDay")
    case 5:
        print("This is Thursday")
    case 6:
        print("This is Friday")
    case 7:
        print("This is saturday")
    case _:
        print("Please Enter a valid day no")
    

match day_no:
    case 1 | 2|3|4|5|6|7:    # | is known as the pipe character
        print("This is a weekday")  
    case _:
        print("Please Enter a valid number")

# We can combine match with if statemetns also

print("Thank you ")