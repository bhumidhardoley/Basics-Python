# Functions in simple term are the actions that a computer language will know how to perform 
# For example the printf() is a function that takes arguments .strings and displays the strings
# Another example can be the input() in here it takes arguments and can take input and can also return values 

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


name = input("Enter your name: ")
print("Hello , " + name)
# It is simply like concatenations


print("Helllo ",name) 

# As my understanding in the print statement there are two arguments just like normal functons
# It will be like sum(a,b) where there are two arguments in use exactly in print also there is a string and a variable with 
# which will be used in printing the two strings means just like the sum fucntions it is taking two arguments to print
# Or we can use the end to force the print fuctions to end with the specific thing we want

name = input("Enter your name: ")
print("Hello ",end=" ") # end is a parameter in here
print(name)

# Multiple arguments
print('Apple','banana','guava',sep=",")