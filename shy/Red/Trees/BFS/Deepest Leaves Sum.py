from collections import deque

class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
返回最深的叶节点值sum
'''

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_sum = depth = 0
        # 逗号是为了更清晰地表示这是一个单元素列表。
        queue = deque([(root, 0),])

        while queue:
            node, curr_depth = queue.popleft()

            # 如果到达叶节点
            if node.left is None and node.right is None:
                # 在叶节点判断条件：
                # 如果当前叶节点深度>记录的深度depth，说明到达了更深的叶节点
                # 题目要求得到最深的叶节点值的和
                if depth < curr_depth:
                    # 赋值deepest_sum，相当于更新为第一个到达的更深的叶节点值，方便后续累加
                    deepest_sum = node.val
                    # 更新depth
                    depth = curr_depth
                # 如果后续访问的叶节点深度相同，累加
                # 如果更深，则执行第一个if
                # 更浅则忽略

                # 逻辑就是每次遇到叶节点，根据其深度判断条件

                elif depth == curr_depth:
                    deepest_sum += node.val

            else:
                # BFS常规步骤。每次append同时记录节点的对应深度（root按0计算）
                if node.left:
                    queue.append((node.left, curr_depth + 1))
                if node.right:
                    queue.append((node.right, curr_depth + 1))

        return deepest_sum
