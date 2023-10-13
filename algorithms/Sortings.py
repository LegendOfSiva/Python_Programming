def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def merge_arrays(arr1, arr2):
    result = []
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            result.append(arr1[ptr1])
            ptr1 += 1
        else:
            result.append(arr2[ptr2])
            ptr2 += 1
    result.extend(arr1[ptr1:])
    result.extend(arr2[ptr2:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_arrays(left, right)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []
    middle = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))
print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))
print(merge_sort([64, 34, 25, 12, 22, 11, 90]))
print(quick_sort([64, 34, 25, 12, 22, 11, 90]))
