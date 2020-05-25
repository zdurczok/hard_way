from dllist import DoubleLinkedList

def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
    # start off assuming it's sorted
        is_sorted = True
        # comparing 2 at a time, skipping ahead
        node = numbers.begin.next
        while node:
            # loop through comparing node to the next
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                # oops, looks like we have to scan again
                is_sorted = False
            node = node.next
        # this is reset at the top but if we never swapped, it's sorted
        if is_sorted: break

def merge_sort(dllist):

    if dllist.count() == 1:
        return dllist

    right = DoubleLinkedList()
    left = DoubleLinkedList()

    middle = dllist.count() // 2
    right_size = middle
    left_size = dllist.count() - middle

    splitting_dllist(dllist, right, right_size)
    splitting_dllist(dllist, left, left_size)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(right, left)

def merge(right, left):
    result = DoubleLinkedList()
    while right.count() != 0 and left.count() != 0:
        if right.begin.value <= left.begin.value:
            result.push(right.unshift())
        else:
            result.push(left.unshift())

    while right.count() != 0:
        result.push(right.unshift())

    while left.count() != 0:
        result.push(left.unshift())

    return result


def splitting_dllist(dllist, splitted_list, dllist_size):

    i = 0
    while i < dllist_size:
        node = dllist.unshift()
        splitted_list.push(node)
        i += 1

    return splitted_list


def get_node_index(some_list, i):
    count = 0
    cur_node = some_list.begin

    while count < i:
        count += 1
        cur_node = cur_node.next
    return cur_node


def quick_sort_partition(some_list, low, high):
    i = low - 1
    pivot = get_node_index(some_list, high)

    for j in range(low, high):
        node_at_j = get_node_index(some_list, j)
        if node_at_j.value <= pivot.value:
            i += 1
            node_at_i = get_node_index(some_list, i)
            node_at_i.value, node_at_j.value = node_at_j.value, node_at_i.value

    node_at_i = get_node_index(some_list, i + 1)
    node_at_high = get_node_index(some_list, high)
    node_at_i.value, node_at_high.value = node_at_high.value, node_at_i.value

    return i + 1

def quick_sort(some_list, low=0, high=None):
    if high == None:
        high = (some_list.count() - 1)
    if low < high:
        p_index = quick_sort_partition(some_list, low, high)
        quick_sort(some_list, low, p_index - 1)
        quick_sort(some_list, p_index + 1, high)
