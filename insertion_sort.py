def insertion_sort(lst):
    for i in range(1,len(lst)):
        while lst[i] < lst[i-1] and i > 0:
            lst[i-1],lst[i] = lst[i],lst[i-1]
            i = i - 1
    return lst
x = insertion_sort([2,4,1,6,2,4])
print(x)

