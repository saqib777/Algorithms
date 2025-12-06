Insertion sort is built around the idea of how people naturally sort playing cards in their hand. You pick one card at a time and insert it into its proper position among the cards that are already sorted. The algorithm applies the same logic to arrays.

At the start, the first element is treated as already sorted because a single element is always sorted by itself. The algorithm then takes the second element and compares it with the first. If it is smaller, it is shifted to the left. At this point, the first two elements become a sorted section. From here on, the algorithm grows this sorted section one element at a time.

For every new element, the algorithm temporarily stores its value and begins comparing it with the elements in the sorted section, starting from the rightmost side. As long as the elements in the sorted section are larger than the current value, they are shifted one position to the right. Once the correct spot is found, the stored value is placed into that position. This process repeats until the entire array becomes sorted.

What makes insertion sort interesting is that it does not swap aggressively like bubble sort. Instead, it shifts elements and inserts the value directly into its correct position. This gives it better performance on nearly sorted data. If the array is already almost in order, insertion sort runs very fast.

Internally, the structure always looks like this: one growing sorted region on the left, and an unsorted region on the right. With each pass, exactly one element moves from the unsorted section into the correct position in the sorted section.

In terms of performance, the worst-case time complexity of insertion sort is O(n²), which occurs when the array is sorted in reverse order. The best case is O(n), which happens when the array is already sorted, because no shifting is required. The space complexity is O(1) since it sorts the array in place without using extra memory.

Insertion sort is stable, meaning that it preserves the relative order of equal elements. It is also adaptive, which makes it faster than bubble sort and selection sort on partially sorted data. This is why insertion sort is often used as a helper algorithm inside more advanced sorting techniques like Tim Sort.

From a learning perspective, insertion sort is extremely valuable because it teaches how local ordering works, how shifting is different from swapping, and how sorted regions grow step by step. It builds a strong foundation for understanding advanced sorting strategies later on.
