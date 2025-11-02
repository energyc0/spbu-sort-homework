def quick_sort(array: list) -> list:
    """
    Quick sort algorithm.
    """
    if len(array) <= 1:
        return array

    def partition(array: list) -> tuple[list, int]:
        """
        Take pivot element and partition the list,
        Return array and position of the element
        that is on the right position.
        """
        pivot = array[-1]
        result = 0
        for i in range(len(array) - 1):
            if array[i] < pivot:
                array[i], array[result] = array[result], array[i]
                result += 1

        array[-1], array[result] = array[result], array[-1]
        return array, result

    array, pivot = partition(array)
    # Sort other parts of the array
    array[:pivot] = quick_sort(array[:pivot])
    array[pivot + 1 :] = quick_sort(array[pivot + 1 :])
    return array
