# Append() it adds value to the end of the list

even = [2,4,6,8]
even.append(10)
print(even)

# extend() it can add multiple values at the end of the list

even.extend([12,14,16]) # So far I have seen that to enter numbers in a list we have to use square brackets
print(even)

# insert() adds element at te specifix position

even.insert(0,0)   # first number is the index second value is the value 
print(even)

# clear() removes all the items from the list

even.clear()
print(even)


# We can update list by simply accessing the index