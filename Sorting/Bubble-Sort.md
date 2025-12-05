Selection sort follows a clear and predictable structure, and breaking it down helps you understand why it behaves the way it does.

At a high level, the algorithm treats the array as two sections: the sorted part on the left and the unsorted part on the right. Initially, the sorted section is empty. With every pass, one element is placed in its correct position, gradually expanding the sorted portion.

The process begins by assuming the first element of the unsorted section is the smallest. You then scan the remaining elements to check if any value is smaller. If a smaller value appears, you update the position of the minimum. After completing the scan, you swap the smallest value with the first element of the unsorted section. This locks that smallest value into its final position.

The algorithm then shifts the boundary forward and repeats the same pattern: locate the smallest element from the remaining unsorted values, bring it to the front, and grow the sorted portion step by step.

What makes selection sort easy to reason about is that it always performs the same number of comparisons, even if the list is nearly sorted. It doesn’t try to be adaptive or clever; it simply looks for the smallest element every single time. The trade-off is that it runs slowly on large inputs, but it performs very few swaps, which can be useful in situations where swapping is expensive.

The core structure of the algorithm can be summarized as:

1. Start with the entire list as unsorted.
2. Find the smallest value in the unsorted portion.
3. Swap it into the correct position at the beginning of the unsorted section.
4. Mark that position as sorted.
5. Repeat until no unsorted elements remain.

This step-by-step expansion of the sorted section is what defines selection sort.

```
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print("Original:", sample)
    print("Sorted:", selection_sort(sample))
```
