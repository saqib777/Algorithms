# Algorithm: Stack
# Time Complexity:  O(n) — single pass through string
# Space Complexity: O(n) — stack stores at most n/2 brackets

def is_valid(s: str) -> bool:
    """
    Return True if the string has valid bracket pairs.
    Every opening bracket must be closed in the correct order.

    Supported pairs: () [] {}
    """
    stack    = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0


# ── test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(is_valid("()"))        # True
    print(is_valid("()[]{}"))    # True
    print(is_valid("(]"))        # False
    print(is_valid("([)]"))      # False
    print(is_valid("{[]}"))      # True
    print(is_valid(""))          # True
    print(is_valid("["))         # False
