from random import randint
def insertion_sort(my_list):
    for i in range (1,len(my_list)):
        key=my_list[i]
        l=key            #FOR STRINGS SORTING USE l=len(key)
        j=i-1
        while j>=0 and l < my_list[j]: #FOR STRING SORTING while j>=0 and l<=len(my_list[j])
            my_list[j+1]=my_list[j]
            j=j-1
        else:
            my_list[j+1]=key
    return my_list
my_list=[]
for i in range(0,100):
    n = random.randint(1,100)
    my_list.append(n)
print("BEFORE SORTING",my_list)
insertion_sort(my_list)
print("AFTER SORTING",my_list)
