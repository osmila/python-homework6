import random


def bubble_sort(l):
    t = l.copy()
    for n in range(0, len(t)):
        # for i in range(len(t) - n):
        #     if t[i] > t[n]:
        #         t[i], t[n] = t[n], t[i]
        # Bubble sort compares pairs of elements: 0,1 then 1,2 then 2,3 etc so that the biggest one will be at the end and in the next iteration
        # Commented option compares each element with first
        for i in range(len(t) - n - 1):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
    return t


def print_bubble_sort_result():
    nums = [4, 1, 6, 3, 2, 7, 8]
    sorted_list = bubble_sort(nums)
    print(sorted_list)
    list_test = [random.randint(-10, 10) for _ in range(5)]
    print(f'Initial list is:\t{list_test}')
    sorted_list = bubble_sort(list_test)
    print(f'Sorted list is:\t{sorted_list}')


# Tests
# No sorting is needed
actual_nosort = bubble_sort([1, 2, 3])
expected_nosort = [1, 2, 3]
assert actual_nosort == expected_nosort

# Elements are unique
actual_unique = bubble_sort([2, 1, 3, 0, 5, 4])
expected_unique = [0, 1, 2, 3, 4, 5]
assert actual_unique == expected_unique

# Duplicated elements
actual_duplicated = bubble_sort([2, 2, 1, 5, 5, 4])
expected_duplicated = [1, 2, 2, 4, 5, 5]
assert actual_duplicated == expected_duplicated

# Negative numbers
actual_negative = bubble_sort([-2, 0, -1, 5, -5, 4])
expected_negative = [-5, -2, -1, 0, 4, 5]
assert actual_negative == expected_negative

# Empty list
actual_empty = bubble_sort([])
expected_empty = []
assert actual_empty == expected_empty
