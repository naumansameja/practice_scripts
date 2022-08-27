def bubble_sort(lst):
    a = 0
    x = len(lst)
    while a < x:
        i = 1
        while i < x:
            if lst[i] < lst[i-1]:
                lst[i-1],lst[i] = lst[i],lst[i-1]
            i = i + 1
        a = a + 1


lst = [10,6,5,3,2]
bubble_sort(lst)
print(lst)