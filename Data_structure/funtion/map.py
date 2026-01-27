#  map function applies a function to all the elements of an iterable

s = ['1','2','3','4','5']
intN = map(int,s)   # it is an map object not an list
intN = list(intN)
print(intN)

def double(l):
    return l *2

talking = list(map(double,intN))
print(talking)

a = [1,2,3]
b = [4,5,6]

res = list(map(lambda x , y: x+y,a,b))

print(res)

lower = ['apple   ','banna','cherry']
upper = list(map(str.upper,lower))
print(upper)

# We can use this to extract the first letter 

firstLetter = list(map(lambda s: s[0],upper))
print(firstLetter)

nowhite = list(map(lambda s:s.strip(),upper))
print(nowhite)

# Calculate ferenhite from the celcius also 

c = [0,20,30,40]
f = list(map(lambda c: (c*9/5)+32,c))
print(f)