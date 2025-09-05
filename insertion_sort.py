def insertion_sort_desc(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # element to be placed in correct position
        j = i - 1

        # Move elements of arr[0..i-1], that are smaller than key,
        # one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Place key in the right spot
    
    return arr


# Example usage
numbers = [12, 4, 7, 9, 1, 3, 32, 65, 3, 8, 69, 2, 55, 99, 10]
print("Original array:", numbers)
sorted_numbers = insertion_sort_desc(numbers)
print("Sorted array descending:", sorted_numbers)
