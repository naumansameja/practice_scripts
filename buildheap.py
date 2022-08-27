def buildheap(lst,i):
    l = (2 * i)+1
    r = (2*i)+2
    largest = i

    if l < len(lst) and lst[l]>lst[i]:
        largest = l
    if r < len(lst) and lst[r] > lst[largest]:
        largest = r
    if largest != i:
        lst[i],lst[largest] = lst[largest],lst[i]
        buildheap(lst,largest)
lst = [2,3,1,7,8,6]
n = int(len(lst))
index = int((n/2)-1)

while index >= 0:
    buildheap(lst, index)
    index = index - 1
print(lst)