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

matrix = [ [1,2,3],[4,5,6],[7,8,9]]
newMatrix = [val for row in matrix for val in row]
print(newMatrix)

# In list comprehension the logic is exactly same with the for loop for example

m = [[ 11,12,13],[14,15,16],[17,18,19]]
newM = [ ]
for row in m: 
    for val in row:
        newM.append(val)
print(newM)

# (In my understanding): It just keeps all the codes in one line instead of using indentations