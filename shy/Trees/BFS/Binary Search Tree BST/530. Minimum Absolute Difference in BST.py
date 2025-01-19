class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
给定一个二叉搜索树的根节点，
返回树中任意两个不同节点值之间的最小绝对差值。
'''

class Solution:
    def getMinimumDiff(self, root: TreeNode) -> int:

        # 在一个排序的序列中，相邻的两个值之间的差值一定是所有差值中的最小值之一
        def dfs(node):
            if not node:
                return

            # 在二叉搜索树中使用中序遍历
            # 中序遍历-会第一个记录最左边的最深节点，然后每次回退到分支时，探索分支的右边节点
            # 由于二叉搜索树的 node.left.value < node.value < node.right.value，中序遍历此时会提取二叉搜索树的节点值并按升序排序。
            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)


        values = []
        dfs(root)
        ans = float('inf')
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i-1])

        return ans


    def solution2(self, root: TreeNode) -> int:
        # 以迭代实现中序遍历
        # 若当前节点不为None则入栈，并继续向左迭代，以便首先到达树左下角
        # 若为None则记录values，并向右回退迭代，以便按中序遍历存储升序排序结果
        def iterative_inorder(root):
            stack = []
            values = []
            curr = root

            while stack or curr:
                if curr:
                    stack.append(curr)
                    curr = curr.left

                else:
                    curr = stack.pop()
                    values.append(curr.val)
                    curr = curr.right

            return values

        values = iterative_inorder(root)
        ans = float('inf')
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i-1])

        return ans
