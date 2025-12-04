```
# Bubble Sort Implementation

Explanation:
 Bubble Sort works by repeatedly stepping through the list, comparing
 adjacent elements and swapping them if they are out of order. Over multiple
 passes, the largest elements gradually "bubble up" to the end of the list.

 How it works step-by-step:
 1. Start from the beginning of the list.
 2. Compare each pair of adjacent items.
 3. If the first item is larger than the second, swap them.
 4. Continue until the end of the list. After one full pass, the largest
 element is guaranteed to be at the last position.
 5. Repeat the process for the remaining unsorted portion of the list.

 Complexity:
 - Worst Case: O(n^2)
 - Average Case: O(n^2)
 - Best Case: O(n) when the list is already sorted, because the algorithm
 detects no swaps and stops early.

 Notes:
 - Bubble Sort is simple to understand but inefficient for large datasets.
 - The early exit optimization (checking if a swap happened) improves its
 performance on nearly-sorted lists.
 - Good for learning how comparison-based sorting works, but rarely used
 in production due to higher time complexity compared to algorithms like
 Merge Sort or Quick Sort.


 This function takes a list of numbers and returns a sorted version of it
 using the Bubble Sort algorithm.
```
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

