# PALISSON Antoine

## Linear Search
def linear_search(arr, x):

    for i in range(0, len(arr)): 
        if arr[i] == x : 
            return i 
        
    return -1

def linear_search_duplicates(arr, x):
    findings = [] 

    for i in range(0, len(arr)):
        if arr[i] == x : 
            findings.append(i) 

    return findings

## Binary Search 
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)


def binary_search_duplicates(arr, low, high, x):
    """
    It's important to note that while this maintains the general efficiency 
    of binary search for finding one instance of the target, 
    the need to find all target instances might result in a performance 
    closer to linear search in cases where the target occurs frequently.
    """
    if high < low:
        return []
    
    mid = (high + low) // 2

    if arr[mid] == x:
        findings = [mid]
        findings.extend(binary_search_duplicates(arr, low, mid - 1, x))
        findings.extend(binary_search_duplicates(arr, mid + 1, high, x))    
        return findings
    elif arr[mid] > x:
        return binary_search_duplicates(arr, low, mid - 1, x)
    else :
        return binary_search_duplicates(arr, mid + 1, high, x)

## BST Search 
# see Correction_BST_dict.py

if __name__ == "__main__":
    arr = [-8, -6, -5, -4, -1, 2, 4, 5, 5, 8, 9]
    print(f"linear search     : {linear_search(arr,x=5)}")
    print(f"linear duplicates : {linear_search_duplicates(arr,x=5)}")
    print(f"binary search     : {binary_search(arr,low=0,high=len(arr),x=5)}")
    print(f"binary duplicates : {binary_search_duplicates(arr,low=0,high=len(arr),x=5)}")

    