class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

class Solution:
    # dfs
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(node, small, large):
            if not node:
                return True

            if not (small < node.val < large):
                return False

            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)

            return left and right

        return dfs(root, float('-inf'), float('inf'))


    # iteration
    def solution2(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, small, large = stack.pop()
            if not (small < node.val < large):
                return False

            if node.left:
                stack.append((node.left, small, node.val))
            if node.right:
                stack.append((node.right, node.val, large))

        return True