from collections import deque

class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
 (i.e., from left to right, then right to left for the next level and alternate between).
'''

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        ans = []
        level_list = deque()

        if root is None:
            return []

        node_queue = deque([root, None])
        is_order_left = True

        while node_queue:
            curr_node = node_queue.popleft()
            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)

            else:
                # 转换为list而非deque，方便验证答案格式
                ans.append(list(level_list))


                # 如果node_queue非空，说明还有下一层节点待处理。
                # 此时append None，给下一层节点打上结束标记
                if node_queue:
                    node_queue.append(None)

                level_list = deque()
                is_order_left = not is_order_left

        return ans
