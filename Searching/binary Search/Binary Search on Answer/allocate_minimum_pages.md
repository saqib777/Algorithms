# Allocate Minimum Pages

## Problem Statement

You are given an array `books` where each element represents the number of pages in a book, and an integer `students` representing the number of students.

Your task is to allocate books to students such that:

1. Each student gets **at least one book**.
2. Each book is allocated to **only one student**.
3. Books must be allocated in **contiguous order**.
4. The goal is to **minimize the maximum number of pages assigned to any student**.

Return the **minimum possible maximum pages**.

If allocation is not possible, return `-1`.

---

## Example

Input:

```python
books = [12, 34, 67, 90]
students = 2
```

Output:

```python
113
```

Explanation:

Possible allocation:

Student 1 → 12 + 34 + 67 = 113
Student 2 → 90

Maximum pages = 113 (minimum possible)

---

## Intuition

This is another classic:

> Minimize the maximum value

Whenever you see this pattern, think:

```python
Binary Search on Answer
```

We are not searching for an index.

We are searching the **maximum pages limit** that a student can receive.

---

## Search Space

Minimum possible pages:

```python
max(books)
```

Because one student must take the largest book.

Maximum possible pages:

```python
sum(books)
```

One student takes all books.

So:

```python
low = max(books)
high = sum(books)
```

---

## Feasibility Logic

We check:

> Can we allocate books so that no student gets more than `mid` pages?

Greedy allocation:

* Keep assigning books until limit exceeds `mid`
* Then assign to next student

If students required ≤ given students → valid

Else → invalid

---

## Algorithm (Binary Search on Answer)

1. If students > number of books → return -1

2. Initialize:

```python
low = max(books)
high = sum(books)
```

3. While `low <= high`:

Find mid:

```python
mid = (low + high) // 2
```

Check feasibility.

If valid:

```python
answer = mid
high = mid - 1
```

Try smaller maximum.

Else:

```python
low = mid + 1
```

4. Return answer.

---

## Dry Run

Books:

```python
[12, 34, 67, 90]
students = 2
```

Search space:

```python
low = 90
high = 203
```

Mid = 146 → possible → try smaller

Mid = 117 → possible → try smaller

Mid = 103 → not possible → increase

Mid = 113 → possible → answer

Final result = 113

---

## Python Implementation

```python
def allocate_minimum_pages(books, students):

    if students > len(books):
        return -1

    def can_allocate(max_pages):
        required_students = 1
        current_pages = 0

        for pages in books:
            if current_pages + pages > max_pages:
                required_students += 1
                current_pages = pages
            else:
                current_pages += pages

        return required_students <= students

    low = max(books)
    high = sum(books)
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if can_allocate(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


# Example usage
books = [12, 34, 67, 90]
students = 2

print(allocate_minimum_pages(books, students))  # Output: 113
```

---

## Time Complexity

Binary search range:

```python
O(log(sum(books)))
```

Feasibility check:

```python
O(n)
```

Overall:

```python
O(n log(sum))
```

---

## Space Complexity

```python
O(1)
```

No extra memory used.

---

## Key Learning

Important pattern:

> Aggressive Cows → Maximize minimum
> Allocate Pages → Minimize maximum

Both use:

```python
Binary Search on Answer
```

Only feasibility logic changes.

---

## Interview Tip

Whenever you see:

* Work distribution
* Load balancing
* Minimize maximum effort
* Split into k parts

Think Binary Search on Answer.

---

## Related Problems

* Aggressive Cows
* Koko Eating Bananas
* Capacity to Ship Packages Within D Days
* Split Array Largest Sum
