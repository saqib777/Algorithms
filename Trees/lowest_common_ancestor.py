# Algorithm: DFS Recursive (Post-order)
# Time Complexity:  O(n) — may visit all nodes in worst case
# Space Complexity: O(h) — h = height of tree (recursion stack)

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor (LCA) of two nodes p and q
    in a binary tree (not necessarily a BST).

    LCA is the deepest node that has both p and q as descendants,
    where a node is considered a descendant of itself.

    Key insight (post-order):
    - If current node is p or q, return it.
    - Recurse left and right.
    - If both sides return non-null, current node is the LCA.
    - If only one side is non-null, propagate that up.
    """
    if not root:
        return None
    if root is p or root is q:
        return root

    left  = lowest_common_ancestor(root.left,  p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root   # p is in one subtree, q in the other

    return left if left else right


def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Optimised version for BST (not general binary tree).
    Uses BST ordering property to avoid unnecessary traversal.
    Time: O(h) — only travels one path down the tree.
    """
    while root:
        if p.value < root.value and q.value < root.value:
            root = root.left
        elif p.value > root.value and q.value > root.value:
            root = root.right
        else:
            return root
    return None


if __name__ == "__main__":
    #           3
    #          / \
    #         5   1
    #        / \ / \
    #       6  2 0  8
    #         / \
    #        7   4
    n7 = TreeNode(7); n4 = TreeNode(4)
    n6 = TreeNode(6); n2 = TreeNode(2, n7, n4)
    n0 = TreeNode(0); n8 = TreeNode(8)
    n5 = TreeNode(5, n6, n2)
    n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)

    print(lowest_common_ancestor(root, n5, n1).value)  # 3
    print(lowest_common_ancestor(root, n5, n4).value)  # 5
    print(lowest_common_ancestor(root, n6, n4).value)  # 5
