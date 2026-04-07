
# Longest Substring Without Repeating Characters  Variable Sliding Window

After learning fixed-size sliding windows, the next step is to handle windows that **grow and shrink dynamically**.

This problem is one of the most important examples of that idea.

---

## The Problem

Given a string `s`, find the length of the **longest substring without repeating characters**.

Example:

```id="x9a2bc"
s = "abcabcbb"
```

Output:

```id="y8k1pl"
3
```

Explanation:

```id="m4z7qd"
"abc" is the longest substring without repeating characters
```

---

Another example:

```id="p2n8tx"
s = "bbbbb"
```

Output:

```id="q1v4yu"
1
```

---

## Key Idea

We use a **sliding window** with two pointers:

* `left` → start of window
* `right` → end of window

We expand the window by moving `right`.

If a duplicate is found, we **shrink the window from the left** until it becomes valid again.

---

## Why We Need a Hash Set

To quickly check if a character is already inside the window, we use a set.

This allows:

* O(1) lookup
* Efficient duplicate detection

---

## Algorithm

1. Initialize:

   * `left = 0`
   * empty set
   * `max_length = 0`

2. Move `right` pointer across the string

3. If character is already in set:

   * Remove characters from left until duplicate is gone

4. Add current character to set

5. Update maximum length

---

## Python Implementation

```python id="d8v3xm"
def longest_unique_substring(s):

    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Example
s = "abcabcbb"

print(longest_unique_substring(s))
```

Output:

```id="k7q9wx"
3
```

---

## Time Complexity

Each character is added and removed at most once.

```id="w2z8mr"
O(n)
```

---

## Space Complexity

Set stores characters.

```id="h4t9eq"
O(k)
```

Where `k` is the size of unique characters.

---

## Why This Problem Is Important

This problem introduces **variable sliding window**, which is far more powerful than fixed window.

It is used in many advanced problems such as:

* Longest substring with at most K distinct characters
* Minimum window substring
* Longest repeating character replacement

Mastering this pattern is a big step in DSA.
