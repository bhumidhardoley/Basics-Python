# There are many many many execptions are there in python but only few will be discussed in here

try:
    number = int(input("Enter a number only: ")) # we try to only add the lines which may return error
    # print(f"You entered : {number}")
except ValueError:   # In here we can use multiple Errors

    # print('You must enter only numbers')
    # If you want to not print anything after an error you can just use the pass kewrod 
    pass  # what it will do is just check for the erro and pass


else: 
    print(f'You entered {number}')


choice = 1

while choice:
    try:
        newNumber = int(input("Enter a number only: "))
    except ValueError:
        print("You can Enter a number only ")
        choice = int(input("wanna try again (1/0): "))
    else:
        print(f"You entered {newNumber}")
        choice = 0