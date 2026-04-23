# Algorithm: Iterative Preorder using Explicit Stack
# Time Complexity:  O(n) — every node visited once
# Space Complexity: O(h) — stack depth equals tree height

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def preorder_recursive(root: TreeNode) -> list[int]:
    """
    Root → Left → Right.
    Recursive — intuitive and clean.
    """
    result = []

    def traverse(node):
        if not node:
            return
        result.append(node.value)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result


def preorder_iterative(root: TreeNode) -> list[int]:
    """
    Iterative using a stack.
    Push right child before left so left is processed first.
    """
    if not root:
        return []

    result = []
    stack  = [root]

    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


if __name__ == "__main__":
    root = TreeNode(4,
             TreeNode(2, TreeNode(1), TreeNode(3)),
             TreeNode(6, TreeNode(5), TreeNode(7)))

    print(preorder_recursive(root))  # [4,2,1,3,6,5,7]
    print(preorder_iterative(root))  # [4,2,1,3,6,5,7]
