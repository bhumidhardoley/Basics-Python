value = int(input("Loop starts from 0 and goes to 100 you want to stop that at: "))
i = 1
while i<= 100:
    if i == value:
        break
    print(i,end=' ') 
    i +=1 

# since I am breaking at the value that step will be skipped completely