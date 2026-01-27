# if we have a list we can access it through the index

names = ['Horizeon','Paimon','Rubby','Pyro']
print(names[2])  # if only means the element present in there
print(names[1:2])
print(names[-2])
print(names[::-1])

# There is square brackets in the output if  we use multiple indexing if only one then no square brackets

numbers = [0,1,2,3,4,5]
print(numbers[-1:-5:-1])

# New thing here is that if you want to move left to right no steps needed python assumes it to be one but in case of the right to left you have to provide index

name = 'Hello'
print(name[::-1])

# When we try to move backwards then it just adds the steps back and that's important thing