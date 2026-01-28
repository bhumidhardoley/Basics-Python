# tuples in python are order immutable collection of elements

numbers = ('a','b','c','d')
a = numbers.count('a')
print(a)


# tuples are created using the ( ) and it can have any number off elements even 0

tup = ()  # correct
nTup = tuple((1,2,3,4))
print(tup)
print(nTup)

names = tuple(('Hello','no'))
print(names)
name = tuple('Hello')
print(name)

without = 'hello','name','this'
print(type(without))

for number in numbers:
    print(number)