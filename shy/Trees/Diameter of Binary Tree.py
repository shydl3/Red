
class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
该题的目标是求二叉树的直径，定义为树中任意两个节点之间最长路径上的边数。这个路径可以经过根节点，也可以不经过根节点。
The length of a path between two nodes is represented by the number of edges between them.
'''

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def longest_path(node: TreeNode) -> int:
            # 递归到最深时返回0
            if not node:
                return 0

            nonlocal diameter
            # 递归计算左右所有可能的分支中，最长路径
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # 每层递归都会更新全局答案：直径是左右子树路径长度之和（即从左子树最深节点到右子树最深节点的路径长度）。
            diameter = max(diameter, left_path + right_path)

            # 递归向上返回时，在每次分支合并时返回左右两边最长的边数
            # 从而合并每种情况的最优值，使最初开始递归的上级节点得到其左右所有分支方向的最优值
            # 并且在每层递归检查更新全局答案
            return max(left_path, right_path) + 1

        # 手动从root开始递归
        longest_path(root)
        return diameter

