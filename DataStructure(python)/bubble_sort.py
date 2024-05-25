# Bubble sort
# Time complexity = O(n^2)

def bubble_sort(arr:list[int])->list:
    """Return sorted array using bubble sort method

    Args:
        arr (list[int]): array of unsorted list

    Returns:
        list: array of sorted list.
    """
    n = len(arr) # size of the array

    # Iteration through the size of the array
    for i in range(0,n):

        for j in range(0, n-1-i):
            # starting from 0 to n-1-i the -i indicated that i elements sorted.
            # if the left side element is greater than the right
            # swap them.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == "__main__":
    arr = [55, 10, 12, 89, 51, 20, 11]
    print("Before sorting:\n",arr)
    arr = bubble_sort(arr)
    print("After sorting:\n",arr)
