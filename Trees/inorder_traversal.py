# Algorithm: DFS with Global Maximum Tracking
# Time Complexity:  O(n) — each node visited once
# Space Complexity: O(h) — recursion stack depth equals tree height

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Return the diameter of the binary tree.

    The diameter is the length of the longest path between
    any two nodes — measured in number of edges.
    The path does not need to pass through the root.

    Key insight: at any node, the longest path through it
    = height(left subtree) + height(right subtree).
    We track the global maximum across all nodes.
    """
    max_diameter = [0]  # use list to allow mutation inside nested function

    def height(node) -> int:
        if not node:
            return 0
        left_h  = height(node.left)
        right_h = height(node.right)
        max_diameter[0] = max(max_diameter[0], left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter[0]


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3))
    print(diameter_of_binary_tree(root))   # 3  (path: 4-2-1-3 or 5-2-1-3)

    root2 = TreeNode(1, TreeNode(2))
    print(diameter_of_binary_tree(root2))  # 1

    print(diameter_of_binary_tree(None))   # 0
