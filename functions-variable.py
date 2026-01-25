# # Functions in simple term are the actions that a computer language will know how to perform 
# # For example the printf() is a function that takes arguments .strings and displays the strings
# # Another example can be the input() in here it takes arguments and can take input and can also return values 

# # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


# name = input("Enter your name: ").strip().capitalize() # strip() is to remove the white spaces 
# firstName , secondName = name.split(" ") # Will split on the space 
# print("Hello , " + firstName)

# # It is simply like concatenations


# # print("Helllo ",name) 

# # As my understanding in the print statement there are two arguments just like normal functons
# # It will be like sum(a,b) where there are two arguments in use exactly in print also there is a string and a variable with 
# # which will be used in printing the two strings means just like the sum fucntions it is taking two arguments to print
# # Or we can use the end to force the print fuctions to end with the specific thing we want

# name = input("Enter your name: ")
# name = name.strip().title()
# print("Hello ",end=" ") # end is a parameter in here
# print(name)

# # Multiple arguments
# print('Apple','banana','guava',sep=",")

# # There are escape characters when we want to include some special characters we can use the backlash \

# print("Hello my friend \"Prakash\" ")


# Float calculations simple

x = float(input("Enter a number: "))
y = float(input("Enter a number: "))

z = round(x+y,3) # In here when useing the 3 it only counts towards the decimal points

# If we want to add an comma in the answer then we can follow the 
print(f"{z:,}")

# : the formatting starts from here , is a format specifier which adds comma in every thousands

newZ = x+y
print(f"{newZ:,.2f}") # .2f make the decimal point 2 digit long only

# And also we can pad the answer with 0 for example in format specifier we can add 015 means width 15 and padd with 0

# print(f"{z:015,}") 
print(f"{newZ:,.2%}")  # multiplies the numer with 100 and add % after 2 digits
