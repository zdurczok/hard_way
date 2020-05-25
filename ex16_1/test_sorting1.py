import sorting
from random import randint

max_numbers = 30

def random_list(count):
    numbers = []
    for i in range(count, 0, -1):
        numbers.append(randint(0, 10000))
    return numbers

def test_bubble_sort():
    numbers = random_list(max_numbers)

    lista1 = sorted(numbers)
    lista2 = sorting.bubble_sort(numbers)
    assert lista1 == lista2

def test_merge_sort():
    numbers = random_list(max_numbers)

    lista1 = sorted(numbers)
    lista2 = sorting.merge_sort(numbers)
    assert lista1 == lista2

def test_quick_sort():
    numbers = random_list(max_numbers)

    lista1 = sorted(numbers)
    lista2 = sorting.quick_sort(numbers)
    assert lista1 == lista2

def test_quickSort_inplace():
    numbers = random_list(max_numbers)

    lista1 = sorted(numbers)
    lista2 = sorting.quickSort_inplace(numbers)
    assert lista1 == lista2

test_bubble_sort()
test_merge_sort()
test_quick_sort()
test_quickSort_inplace()
