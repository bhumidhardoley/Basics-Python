

try:
    n = int(input("Enter the value for n: "))
    m = int(input("Enter the value for m: "))

    divison = n / m

except ZeroDivisionError:

    print("Can not be divided by zero")

except ValueError:

    print("Only numbers are allowed in here")

else:

    print(f"The division is {divison}")

finally:

    print("Execution is completed")

# Let's talk about what are exception really 
# these are problems which can be occured during the runtime so as an programmer we should handle them properly
# Some downsides are the code beecomes slow and little bit of complex if many try excpt blocks are there