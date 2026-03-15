
# Valid Palindrome — Checking Symmetry Using Two Pointers

A palindrome is a string that reads the same forward and backward. Examples include words like **“racecar”** and **“madam”**.

But real-world strings may contain punctuation, spaces, and mixed letter cases. The challenge is to determine whether a string is still a palindrome after ignoring those extra characters.

This problem is a great example of applying the **Two Pointer technique** to string processing.

---

## The Problem

Given a string `s`, determine whether it is a palindrome.

While checking:

* Ignore **non-alphanumeric characters**
* Ignore **letter case**

Return `True` if the string is a palindrome, otherwise return `False`.

Example:

```
s = "A man, a plan, a canal: Panama"
```

Output:

```
True
```

Explanation:

After cleaning the string:

```
amanaplanacanalpanama
```

This reads the same forwards and backwards.

---

## Key Idea

We use two pointers:

* `left` starts at the beginning
* `right` starts at the end

At each step:

1. Skip characters that are not letters or numbers.
2. Compare the characters.
3. Move the pointers inward.

If all characters match, the string is a palindrome.

---

## Algorithm

1. Initialize two pointers:

```
left = 0
right = len(s) - 1
```

2. While `left < right`:

* Skip non-alphanumeric characters
* Compare characters ignoring case
* If they differ → return False
* Move both pointers inward

3. If loop completes → return True

---

## Python Implementation

```python
def is_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Example
s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))
```

Output:

```
True
```

---

## Time Complexity

The string is scanned once.

```
O(n)
```

---

## Space Complexity

No extra memory is required.

```
O(1)
```

---

## Why This Problem Is Important

This problem demonstrates that the **Two Pointer technique is not limited to arrays**. It is also extremely effective for string problems.

Many interview questions involving symmetry or matching characters rely on this idea.
