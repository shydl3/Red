class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

class Solution:
    # recursion
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
# Time complexity : we visit each node exactly once,
# thus the time complexity is O(N), where N is the number of nodes.


    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            if node.left == None and node.right == None:
                return (curr + node.val) == sum

            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right
        return dfs(root, 0)


    # iteration
    def hasPathSum3(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        de = [(root, sum - root.val)]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
        return False
# Time complexity: the same as the recursion approach O(N).