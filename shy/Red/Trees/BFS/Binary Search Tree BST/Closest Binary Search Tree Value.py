from test import target


class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given the root of a binary search tree and a target value,
eturn the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.
'''

class Solution:
    def closestValue(self, root: TreeNode, val: int) -> int:
        def inorder(r: TreeNode):
            # 一行代码返回BST升序排序
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        # Python 中，内置函数 min 可以接受一个可迭代对象（如列表、元组等）和一个可选的 key 参数。
        # 指定 key 时, min(iterable, key=func) 会先用 func 映射每个元素，然后根据映射后的结果来进行比较，最终返回映射结果最小的那个原始元素。
        # lambda x: abs(target - x) 是一个匿名函数，接收一个值 x，返回 x 与 target 的绝对差值。
        return min(inorder(root), key = lambda x: abs(target - x))