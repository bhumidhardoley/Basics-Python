# list Comprehension = short and clean way to create a collection 
# Squaring every number in a list

a = [ 1, 2, 3, 4, 5]
result = [ value **2 for value in a ]  # it creates a list comprehension to create a new list by squaring each number in a 
print(result)

# Example with for loop 

a = [ 1, 2, 3, 4, 5]
res = [ ] # creates an empty list to store results
for val in a:
    res.append(val**2)
print(res)


# Conditional statements in list comprehension

numbers = [1, 2, 3, 4, 5]
res = [ value**2 for value in a if value % 2 == 0 ]
print(res)

# Creating a list from a range

a = [ i for i in range(2,10,2)]
print(a)

# Using nested loops

c = [ (x,y) for x in range(3) for y in range(3)]
print(c)

# Flattening a list of lists

mat = [ [1,2,3],[4,5,6,],[7,8,9]]
res = [val for row in mat for val in row]
print(res)