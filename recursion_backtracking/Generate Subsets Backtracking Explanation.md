Generating all subsets of a set (also called the power set) is the most important introductory problem in backtracking. It shows how recursion is used to explore all possible choices while carefully undoing decisions as the recursion unwinds.

---

Problem Understanding

Given a list of elements, generate all possible subsets.

Example:
Input: [1, 2]
Output: [[], [1], [2], [1, 2]]

For an array of size n, the total number of subsets is 2^n.

---

Core Idea (Include / Exclude)

For every element, you have exactly two choices:

* Include the element in the current subset
* Exclude the element from the current subset

Backtracking explores both choices recursively.

---

What Makes This Backtracking

At each level:

* You make a choice (include an element)
* Explore deeper (recursive call)
* Undo the choice (remove the element)
* Explore the alternative path (exclude)

This pattern of choose → explore → un-choose is the essence of backtracking.

---

Recursive Structure

subsets(index, current_subset)

If index == length of array:
add a copy of current_subset to result
return

Include element at index
Recurse to next index

Exclude element at index (backtrack)
Recurse to next index

---

Step-by-Step Example

Input: [1, 2]

Start with []

Include 1 → [1]
Include 2 → [1, 2] → store
Exclude 2 → [1] → store

Exclude 1 → []
Include 2 → [2] → store
Exclude 2 → [] → store

---

Text-Based Flowchart

Start
→ backtrack(index, current)
→ If index == n
→ store current subset
→ return
→ Include arr[index]
→ backtrack(index + 1, current)
→ Remove last element (backtrack)
→ Exclude arr[index]
→ backtrack(index + 1, current)
→ End

---

Algorithm Structure (Step Form)

1. Initialize empty result list
2. Start recursive backtracking from index 0
3. At each index, include element and recurse
4. Backtrack and exclude element
5. Store subsets when base case is reached

---

Time and Space Complexity

Time Complexity: O(2^n)
Space Complexity: O(n) recursion depth + output space

---

Properties

Does not require sorted input
Generates all combinations
Uses recursion and backtracking

---

When to Use

When exploring all possible combinations
When solving decision-tree style problems

---

Learning Value

This problem teaches the true power of recursion. Once you understand subset generation, you can solve permutations, combinations, and constraint-based problems like N-Queens and Sudoku. This is the foundation of all backtracking algorithms.
