# bubble sort

def bubble_sort(some_list):
    n = len(some_list)

    if n <= 1:
        return some_list
    else:
        while True:
            is_sorted = True
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if some_list[j] > some_list[j+1]:
                        some_list[j], some_list[j+1] = some_list[j+1], some_list[j]
            if is_sorted: break

    return some_list

# merge sort

def merge_sort(some_list):
    if len(some_list) <= 1:
        return some_list

    left = []
    right = []

    for i, elem in enumerate(some_list):
        if i < len(some_list) / 2:
            left.append(elem)
        else:
            right.append(elem)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result

# quick sort, implementation not 'in-place'

def quick_sort(some_list):
    lenght = len(some_list)

    if lenght <= 1:
        return some_list
    else:
        pivot = some_list.pop()

    higher = []
    lower = []

    for item in some_list:
        if item < pivot:
            lower.append(item)
        else:
            higher.append(item)

    return quick_sort(lower) + [pivot] + quick_sort(higher)

# quick sort, implementation 'in-place'

def partition(some_list, low, high):
    i = low - 1
    pivot = some_list[high]

    for j in range(low, high):
        if some_list[j] <= pivot:
            i += 1
            some_list[i], some_list[j] = some_list[j], some_list[i]
    some_list[i+1], some_list[high] = some_list[high], some_list[i+1]
    return i + 1

def quickSort_inplace(some_list, low=0, high=None):
    if high == None:
        high=(len(some_list) - 1)
    if low < high:
        p_index = partition(some_list, low, high)
        quickSort_inplace(some_list, low, p_index - 1)
        quickSort_inplace(some_list, p_index + 1, high)

    return some_list
