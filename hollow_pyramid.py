'''
*
  *
    *
  *
*
  *
    *
  *
*

'''

''' This is the pattern to be printed.

    This function accepts an argument n where n is the input which shows the number of lines to be printed.
'''


def print_pattern(n):
    i = 0
    total_count = 0
    while True:
        while i < 6:
            if total_count == n:
                return
            print(i*' '+"*")
            total_count += 1
            i += 2
        i -= 4
        while i >= 0:
            if total_count == n:
                return
            print(i*' '+"*")
            total_count += 1
            i -= 2
        i += 4


print_pattern(10)
    