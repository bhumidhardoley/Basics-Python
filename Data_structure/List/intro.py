# List are like arrays but more powerfull in python
# They are ordered , index based and mutable
# Lists can be created using square brackets []

numbers = [1,2]  # List of numbers
names = ['Herry','Khusi','Vixen']

for number in numbers:
    print(number)

for name in names:
    print(name)

# We can also use the list() to create lists

evenNumbers = list((2,3,45,4))    # for numbers you have to add another ( ) to make it work 
print(evenNumbers)

rand = list(("Hello",'Nice'))
print(rand)

# If numbers are repeating then we can use the multiplication operator to create it 

a = [2]*7
print(a)
