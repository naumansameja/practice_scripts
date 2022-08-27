def main():
    arr = [25,15,10,81,7,6,5,4]
    n = len(arr)
    print(heapsort(arr))
def buildheap(arr, n, i):
    l = (2 * i)+1
    r = (2*i)+2
    largest = i
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        buildheap(arr, n, largest)
def heapsort(arr):
    n = len(arr)
    res_lst = []
    for i in range((n//2)-1,-1,-1):
        buildheap(arr, n, i)
    for i in range(n-1,-1,-1):

        res_lst.append(arr[0])
        arr[i], arr[0] = arr[0], arr[i]
        del(arr[i])
        buildheap(arr, i, 0)
    return res_lst
main()