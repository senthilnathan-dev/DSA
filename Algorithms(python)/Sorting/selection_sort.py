# selection sort
# time complexity O(N^2)

def selecttion(arr:list[int])->None:
    """Return sorted list"""
    for i in range(0,len(arr)):
        l_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[l_index]:
                l_index = j

        arr[i], arr[l_index] = arr[l_index], arr[i]

if __name__ == "__main__":
    arr = [55, 10, 12, 89, 51, 20, 11]
    print("Before sorting: ", arr)

    selecttion(arr)
    print("After sorting: ", arr)
