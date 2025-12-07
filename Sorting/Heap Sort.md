Heap sort is a comparison-based sorting algorithm that is built on top of a special data structure called a heap. A heap is a complete binary tree where every parent node follows a specific order relationship with its children. In a max heap, every parent is greater than or equal to its children. In a min heap, every parent is smaller than or equal to its children. Heap sort typically uses a max heap so that the largest element can always be extracted efficiently.

At a conceptual level, heap sort works in two main phases. First, it transforms the input array into a max heap. This ensures that the largest element in the array is always at the root of the heap, which is the first position in the array. Second, it repeatedly removes the largest element from the heap and places it at the end of the array, shrinking the heap size step by step until the entire array is sorted.

If you think about the workflow, it looks like this:

Start with an unsorted array.
Build a max heap from the array.
The largest element is now at the root (index 0).
Swap this root with the last element in the array.
Reduce the heap size by one, since the last element is now in its final sorted position.
Apply heapify to the root again to restore the heap property.
Repeat this process until the heap size becomes one.

The key operation that makes heap sort work is heapify. Heapify is the process of fixing the heap property at a given node, assuming that the subtrees below it already satisfy the heap property. Starting from a node, you compare it with its left and right children. If one of the children is larger than the current node, you swap the current node with the largest child. This process continues downwards until the heap property is restored.

A very important detail is how the initial max heap is built. This is done by applying heapify starting from the last non-leaf node and moving upward to the root. By doing this, the entire array is converted into a valid max heap in linear time.

Text-based flow of heap sort:

Start
→ Build max heap from the array
→ Is heap size greater than 1?
→ Yes:
→ Swap root with last element
→ Reduce heap size by 1
→ Heapify at root
→ Repeat
→ No:
→ Sorting complete
→ End

From a complexity perspective, heap sort always runs in O(n log n) time, regardless of the initial order of the elements. This makes it very predictable. The space complexity is O(1) because it sorts the array in place and does not require extra memory proportional to input size.

Heap sort is not a stable sorting algorithm. The relative order of equal elements is not guaranteed to be preserved. This is a trade-off for its strong worst-case performance and in-place nature.

Compared to merge sort, heap sort saves memory because it does not use extra arrays. Compared to quick sort, heap sort avoids the worst-case O(n²) behavior. However, in practice, heap sort is often slower than quick sort due to weaker cache performance and more complex operations.

From a learning perspective, heap sort is extremely important because it teaches how tree-based data structures work inside arrays, how to enforce structural properties like the heap condition, and how logarithmic operations naturally arise from tree height.
