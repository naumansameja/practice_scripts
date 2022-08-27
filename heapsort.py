def bubblesort(lst):
    n = len(lst)
    for _ in range(n):
        swap(lst,n)
def swap(lst,n):
    for i in range(1,n):
        if lst[i-1] > lst[i]:
            lst[i-1],lst[i] = lst[i],lst[i-1]
lst = [25,15,10,8,7,6,4,18]
bubblesort(lst)
print(lst)