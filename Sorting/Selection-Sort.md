Selection sort works by dividing the list into two parts: the portion that is already sorted and the portion that is still unsorted. You start by assuming the first element is the smallest and then compare it with every other element in the unsorted section. When you find the actual smallest value, you swap it into the correct position. After placing one element, you move the boundary forward and repeat the same process for the next position.

The idea is simple: at every step, pick the minimum value from what’s left and place it where it belongs. It’s easy to understand and predictable in how it behaves, but it isn’t efficient for large datasets because it always performs the same number of comparisons regardless of whether the list is already sorted. The algorithm does, however, make very few swaps, which is one of its small advantages.

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
