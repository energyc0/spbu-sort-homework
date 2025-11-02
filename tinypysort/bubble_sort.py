def bubble_sort(arr: list) -> list:
    """
    Bubble sort algorithm.
    """
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr
