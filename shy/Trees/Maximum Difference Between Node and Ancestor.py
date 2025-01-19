class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
给定一个二叉树的根节点，找到最大值 v，
v 是 |a.val - b.val| 的值，其中 a 是 b 的祖先节点，并且 a 和 b 是不同的节点。
'''

class Solution:
    # 动态维护当前路径上的最优值(与最大、最小值的差)
    # 避免了重复计算
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.result = 0

        def helper(node, curr_max, curr_min):
            if not node:
                return

            self.result = max(self.result, abs(curr_max-node.val), abs(curr_min-node.val))

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            helper(node.left, curr_max, curr_min)
            helper(node.right, curr_max, curr_min)

        help(root, root.val, root.val)
        return self.result


    # 更直接更新路径中的最大值和最小值
    def maxAncestorDiff2(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 这种递归会返回每条单一路径的最大差值，并在返回每次分支的时候，比较左右分支的最优答案 max(left, right)
        # 最终得到全局答案
        def helper(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            left = helper(node.left, curr_max, curr_min)
            right = helper(node.right, curr_max, curr_min)
            return max(left, right)

        return helper(root, root.val, root.val)