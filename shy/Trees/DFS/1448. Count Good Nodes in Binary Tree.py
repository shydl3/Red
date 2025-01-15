'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursion
    # Time complexity: O(n)
    # With DFS we visit every node exactly once and do a constant amount of work each time.
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            nonlocal num_good_nodes
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.left:
                dfs(node.left, max(max_so_far, node.val))
            if node.right:
                dfs(node.right, max(max_so_far, node.val))

        num_good_nodes = 0
        dfs(root, float('-inf'))

        return num_good_nodes


    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]
        num_good_nodes = 0

        while stack:
            node, max_so_far = stack.pop()

            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.left:
                stack.append((node.left, max(max_so_far, node.left.val)))
            if node.right:
                stack.append((node.right, max(max_so_far, node.right.val)))

        return num_good_nodes