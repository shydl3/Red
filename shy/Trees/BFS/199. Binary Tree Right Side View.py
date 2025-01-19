'''
Given the root of a binary tree,imagine yourself standing on the right side of it.
Return the values of the nodes you can see ordered from top to bottom.
'''

from collections import deque

class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This algorithm has a time and space complexity of O(n)
# for the same reasons as the algorithms in the previous article.
# We visit each node only once and perform a constant amount of work at each node. \
# The queue could hold up to O(n) nodes.
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            curr_len = len(queue)
            # 添加最右边的节点值
            ans.append(queue[-1].val)

            # 照常BFS的步骤
            for _ in range(curr_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans