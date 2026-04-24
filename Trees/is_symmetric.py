# Algorithm: BFS Iterative (Mirror Check using Queue Pairs)
# Time Complexity:  O(n) — all nodes visited once
# Space Complexity: O(w) — w = maximum width of the tree

from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def is_symmetric_recursive(root: TreeNode) -> bool:
    """
    A tree is symmetric if its left subtree is a mirror
    of its right subtree.

    Recursive: compare outer and inner pairs simultaneously.
    """
    def mirror(left, right) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.value == right.value
                and mirror(left.left,  right.right)
                and mirror(left.right, right.left))

    return mirror(root.left, root.right) if root else True


def is_symmetric_iterative(root: TreeNode) -> bool:
    """
    Iterative version using a queue of pairs.
    Enqueue mirror pairs together and compare them.
    """
    if not root:
        return True

    queue = deque([(root.left, root.right)])

    while queue:
        left, right = queue.popleft()

        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.value != right.value:
            return False

        queue.append((left.left,  right.right))
        queue.append((left.right, right.left))

    return True


if __name__ == "__main__":
    # Symmetric:     1
    #               / \
    #              2   2
    #             / \ / \
    #            3  4 4  3
    sym = TreeNode(1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)))
    print(is_symmetric_recursive(sym))  # True
    print(is_symmetric_iterative(sym))  # True

    # Asymmetric:    1
    #               / \
    #              2   2
    #               \   \
    #               3    3
    asym = TreeNode(1,
             TreeNode(2, None, TreeNode(3)),
             TreeNode(2, None, TreeNode(3)))
    print(is_symmetric_recursive(asym))  # False
    print(is_symmetric_iterative(asym))  # False
