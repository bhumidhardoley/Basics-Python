# We can use the remove() to remove a specifix item  but only the first occurence

tenth = [20,10,20,30,40,50]
tenth.remove(20)
print(tenth)

# pop() can remove item from a specific position or the last elements if no index proovided

tenth.pop()
print(tenth)

# del statement deltes item at a specific postion
del tenth[2]
print(tenth)