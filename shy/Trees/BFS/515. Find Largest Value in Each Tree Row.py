from collections import deque

class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
返回每个leval所有节点的最大值
'''

class Solution:
    def largstValues(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        while queue:
            curr_len = len(queue)
            curr_max = float('-inf')

            for _ in range(curr_len):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(curr_max)

        return ans






