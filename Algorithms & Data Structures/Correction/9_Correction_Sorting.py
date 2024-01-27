# PALISSON Antoine

## Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        early_stop = True

        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                early_stop = False

        if early_stop : break

    return arr

def bubble_sort_recursive(arr):
    if len(arr) == 1:
        return arr

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return bubble_sort_recursive(arr[:-1]) + [arr[-1]]

## Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def selection_sort_recursive(arr):
    if len(arr) == 1:
        return arr

    min_index = 0
    for j in range(1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[0], arr[min_index] = arr[min_index], arr[0]

    return [arr[0]] + selection_sort_recursive(arr[1:])

## Insertion
def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        target = arr[i]
        j = i - 1

        while j >= 0 and target < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = target

    return arr

def insertion_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    arr[:-1] = insertion_sort_recursive(arr[:-1])

    last = arr[-1]
    j = len(arr) - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

    return arr

## Merge Sort
def merge(left, right):
    arr = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid_point = len(arr) // 2
    left = merge_sort(arr[:mid_point])
    right = merge_sort(arr[mid_point:])

    return merge(left, right)

## QuickSort
def partition(arr, low_idx, high_idx):
    """
    This function sets the elements greater than the pivot on the right 
    and the ones lesser than the pivot on the left.

    Variables:
        > high is the pivot position 
        > pivot is the pivot value
        > high_pos is the location of the highest element (see course)
    """
    pivot = arr[high_idx]
    high_pointer = low_idx

    for low_pointer in range(low_idx, high_idx):
        if arr[low_pointer] <= pivot:
            arr[high_pointer], arr[low_pointer] = arr[low_pointer], arr[high_pointer]
            high_pointer += 1

    # Swap pivot with final high pointer position
    arr[high_pointer], arr[high_idx] = arr[high_idx], arr[high_pointer]

    return arr, high_pointer

def quick_sort(arr, low_idx, high_idx):
    if low_idx < high_idx:
        arr, pivot = partition(arr, low_idx, high_idx)
        quick_sort(arr, low_idx, pivot - 1)         # recursion on the left subarray
        quick_sort(arr, pivot + 1, high_idx)        # recursion on the right subarray

    return arr

if __name__ == '__main__':
    arr = [4,-6,2,0,8,6,9,-5,-7,5,-1,2,3,0]
    print(f"bubble sort    : {bubble_sort(arr.copy())}")
    print(f"selection sort : {selection_sort(arr.copy())}")
    print(f"insertion sort : {insertion_sort(arr.copy())}")
    print(f"merge sort     : {merge_sort(arr.copy())}")
    print(f"quick sort     : {quick_sort(arr.copy(), low = 0, high = len(arr) - 1)}")
