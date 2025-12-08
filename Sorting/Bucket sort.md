Bucket sort is a distribution-based sorting algorithm that works by dividing elements into a number of smaller groups called buckets. Each bucket is then sorted individually, either using another sorting algorithm or recursively using bucket sort itself. Finally, all buckets are merged together to form the final sorted array.

---

Core Idea

Instead of trying to sort everything at once, bucket sort distributes values into ranges (buckets). Each bucket holds values that fall within a specific interval. Since each bucket contains fewer elements and a narrower range, sorting within a bucket becomes very fast.

---

High-Level Workflow

1. Decide the number of buckets.
2. Distribute elements into their respective buckets based on value range.
3. Sort each bucket individually.
4. Concatenate all buckets in order to form the sorted array.

---

Detailed Step-by-Step Example

Input array:
[0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]

Step 1: Create Buckets
If we choose 5 buckets, they may represent these ranges:
Bucket 0 → 0.0 to 0.19
Bucket 1 → 0.2 to 0.39
Bucket 2 → 0.4 to 0.59
Bucket 3 → 0.6 to 0.79
Bucket 4 → 0.8 to 1.0

Step 2: Distribute Elements
Bucket 1: 0.32, 0.33, 0.37
Bucket 2: 0.42, 0.47, 0.51, 0.52

Step 3: Sort Each Bucket
Bucket 1 sorted → [0.32, 0.33, 0.37]
Bucket 2 sorted → [0.42, 0.47, 0.51, 0.52]

Step 4: Merge Buckets
Final sorted array:
[0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]

---

Text-Based Flowchart

Start
→ Create empty buckets
→ Distribute input elements into buckets
→ Sort each bucket individually
→ Merge all buckets in sequence
→ End

---

Algorithm Structure (Step Form)

1. Read input array
2. Initialize N empty buckets
3. For each element
   → Calculate bucket index
   → Insert element into that bucket
4. Sort each bucket
5. Concatenate all buckets
6. Return sorted array

---

Time and Space Complexity

Best Case Time: O(n)
Average Case Time: O(n + k)
Worst Case Time: O(n²) when all elements go into one bucket

Space Complexity: O(n + k)

---

Properties

Bucket sort is stable when stable sorting is used within buckets
Bucket sort is not comparison-based at the distribution level
Bucket sort is not in-place
Bucket sort is highly efficient for uniformly distributed data

---

When to Use

When input is uniformly distributed
When floating point numbers are involved
When range is known and evenly spread

---

When Not to Use

When data is highly skewed
When memory usage must be minimal
When distribution is unknown

---

Learning Value

Bucket sort strengthens understanding of distribution-based sorting, data grouping, and hybrid sorting techniques. It also shows how sorting can be optimized when data follows predictable patterns.

```
def bucket_sort(arr):
    if not arr:
        return arr

    n = len(arr)
    buckets = [[] for _ in range(n)]

    for value in arr:
        index = int(n * value)
        if index == n:
            index -= 1
        buckets[index].append(value)

    for i in range(n):
        buckets[i].sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    for i in range(len(arr)):
        arr[i] = result[i]

    return arr


if __name__ == "__main__":
    sample = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print("Original:", sample)
    print("Sorted:", bucket_sort(sample))

```
