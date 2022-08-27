def merge_sort(lst):
    if len(lst) > 1:
        left_arr = lst[:len(lst)//2]
        right_arr = lst[len(lst)//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                lst[k] = left_arr[i]
                i += 1
            else:
                lst[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            lst[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            lst[k] = right_arr[j]
            j += 1
            k += 1
x = [0,1,4,2,7,3]
merge_sort(x)
print(x)
