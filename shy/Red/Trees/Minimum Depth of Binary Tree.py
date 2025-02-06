class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

'''

from collections import deque

class Solution:
    # DFS
    # Time complexity: O(N)
    # We will traverse each node in the tree only once; hence, the total time complexity would be O(N).
    def minDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0

            # 从存在子节点的一侧继续延申
            if node.left is None:
                return 1 + dfs(node.right)
            elif node.right is None:
                return 1 + dfs(node.left)
            # 如果左右都存在子节点，返回最浅层计数
            return 1 + min(dfs(node.left), dfs(node.right))

        # 从root开始递归即可
        return dfs(root)
