# Algorithm: Iterative Postorder using Two Stacks
# Time Complexity:  O(n) — every node visited once
# Space Complexity: O(n) — two stacks in worst case

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def postorder_recursive(root: TreeNode) -> list[int]:
    """
    Left → Right → Root.
    Most natural use: deleting a tree, evaluating expression trees.
    """
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.value)

    traverse(root)
    return result


def postorder_iterative(root: TreeNode) -> list[int]:
    """
    Iterative using two stacks.
    Stack 1 drives traversal (Root→Right→Left).
    Stack 2 reverses to get Left→Right→Root.
    """
    if not root:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node.value)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    return stack2[::-1]


def postorder_single_stack(root: TreeNode) -> list[int]:
    """
    Iterative using one stack and a 'last visited' pointer.
    More complex but space-optimal single-stack approach.
    """
    result      = []
    stack       = []
    last_visited = None
    current      = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        peek = stack[-1]
        if peek.right and last_visited is not peek.right:
            current = peek.right
        else:
            result.append(peek.value)
            last_visited = stack.pop()

    return result


if __name__ == "__main__":
    root = TreeNode(4,
             TreeNode(2, TreeNode(1), TreeNode(3)),
             TreeNode(6, TreeNode(5), TreeNode(7)))

    print(postorder_recursive(root))     # [1,3,2,5,7,6,4]
    print(postorder_iterative(root))     # [1,3,2,5,7,6,4]
    print(postorder_single_stack(root))  # [1,3,2,5,7,6,4]
