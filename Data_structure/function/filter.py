# In filter() we extract elements from iterables like list , tuples which satisfy a certain condition

# filter(funtion,iterable)

numbers = [1,2,3,4,5,10]

even = list(filter(lambda s:s%2==0,numbers))
print(even)

# Unlike map which creates a new list it just takes out elements from the list (existing)