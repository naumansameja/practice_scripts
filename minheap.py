def minheap(lst, i):
    l = (2*i) + 1
    r = (2*i) + 2
    smallest = i
    if l < len(lst) and lst[l] < lst[i]:
        smallest = l
    if r < len(lst) and lst[r] < lst[smallest]:
        smallest = r
    if smallest != i:
        lst[i],lst[smallest] = lst[smallest], lst[i]
        minheap(lst,smallest)
lst = [2,3,1,7,8,6]
n = int(len(lst))
x = int((n / 2)-1)
while x >= 0:
    minheap(lst,x)
    x = x - 1
print(lst)