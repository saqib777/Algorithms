```
# Bubble Sort Implementation

# This function takes a list of numbers and returns a sorted version of it
# using the Bubble Sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swap happens in this pass
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return arr

# Example usage
if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Sorted:", bubble_sort(sample))
```

