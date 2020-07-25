def isort(a):
    for x in range(1, len(a)):
        k = a[x]
        j = x - 1
        while j >= 0 and k < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k    
        
import random
mylist = []
for i in range(0,100000):
    n = random.randint(1,100)
    mylist.append(n)
print(mylist)
# mylist = input('Enter the list values to be sorted: ').split()
# mylist = [int(x) for x in mylist]
isort(mylist)
print('The sorted list is: ')
print(mylist)
