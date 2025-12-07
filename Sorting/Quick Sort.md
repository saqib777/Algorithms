Quick sort is another divide and conquer algorithm, but unlike merge sort, it does most of its work during the partitioning phase rather than during merging. The core idea is to pick one element as a pivot and then rearrange the array so that all elements smaller than the pivot come to its left, and all elements larger than the pivot come to its right. Once the pivot is in its correct position, the same process is applied recursively to the left and right subarrays.

At the highest level, the workflow of quick sort looks like this:

1. Choose a pivot element from the array.
2. Reorder the array so that all elements less than the pivot are placed before it and all elements greater than the pivot are placed after it.
3. The pivot is now in its final correct position.
4. Recursively apply the same steps to the left subarray and the right subarray.

This continues until all subarrays have size zero or one, which means the array is fully sorted.

The partitioning step is the heart of quick sort. You scan the array and, based on comparisons with the pivot, you rearrange elements in such a way that the pivot naturally ends up where it should be in the final sorted order. After this step, you are guaranteed that everything on the left of the pivot is smaller and everything on the right is larger. There is no need to touch the pivot again.

If you visualize the flow of quick sort, it looks something like this in text form:

Start
→ Choose a pivot
→ Partition the array around the pivot
→ Is the left subarray size greater than 1?
→ Yes: apply quick sort on the left subarray
→ Is the right subarray size greater than 1?
→ Yes: apply quick sort on the right subarray
→ End

Within the partition operation itself, the internal workflow can be understood as:

1. Select a pivot value.
2. Initialize an index that tracks where the next smaller-than-pivot element should go.
3. Scan the array from left to right.
4. Every time you find an element smaller than or equal to the pivot, swap it into the tracked position and move the tracker forward.
5. Finally, place the pivot into its correct position.

Algorithm in detailed step form:

1. If the array has fewer than two elements, return it as already sorted.
2. Select a pivot element. Common choices include the first element, the last element, or the middle element.
3. Partition the array into two parts based on the pivot.
4. Recursively call quick sort on the left partition.
5. Recursively call quick sort on the right partition.
6. Combine the results by placing the pivot between the two sorted partitions.

Quick sort has a very interesting performance profile. In the average case, it runs in O(n log n) time, which makes it extremely fast in practice. However, in the worst case, when the pivot choices are consistently poor (for example, always choosing the smallest or largest element in an already sorted array), the time complexity degrades to O(n²).

The space complexity of quick sort is O(log n) on average due to the recursion stack. In the worst case, it can grow to O(n) if the recursion becomes highly unbalanced.

Quick sort is not a stable sorting algorithm. If two elements have the same value, their original order is not guaranteed to be preserved after sorting. This is one of the trade-offs for its speed.

One of the biggest strengths of quick sort is that it is an in-place sorting algorithm. It does not require large additional memory like merge sort. This makes it very efficient in real-world systems where memory usage matters.

From a learning standpoint, quick sort is extremely important because it ties together recursion, partitioning logic, in-place manipulation, and average-vs-worst-case analysis in one powerful algorithm. Understanding quick sort deeply gives you a strong foundation for analyzing performance and designing efficient algorithms.
