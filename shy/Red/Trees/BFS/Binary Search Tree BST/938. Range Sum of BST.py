'''
Given the root node of a binary search tree and two integers low and high
return the sum of values of all nodes with a value in the inclusive range [low, high].
返回值在 [low, high] 范围内的所有节点的值的总和。
'''

from collections import deque

class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        ans = 0
        if low <= root.val <= high:
            ans += root.val
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)
        if high > root.val:
            ans += self.rangeSumBST(root.right, low, high)

        return ans


    # iterative
    def rangeSumBST2(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            if node.left and low < node.val:
                stack.append(node.left)
            if node.right and node.val < high:
                stack.append(node.right)

        return ans


