
class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

consraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.
'''

class Solution:
    def __init__(self):
        self.ans = None

    # Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(curr_node: TreeNode) -> bool:
            if not curr_node:
                return False

            # recurse_tree会返回布尔值，表示传入的curr_node或其直接left、right子节点是否包含p或q
            # 因此对当前节点curr_node的左右子节点递归调用，用于检查是否遇到p或q
            left = recurse_tree(curr_node.left)
            right = recurse_tree(curr_node.right)

            # 检查当前节点是否为 p 或 q
            mid = (curr_node == p or curr_node == q)

            # 如果当前节点是 p 或 q，或者左右子树都包含 p 或 q，则找到了最近公共祖先
            if mid + left + right >= 2:
                self.ans = curr_node

            # 这里返回的布尔值用于递归返回后判断答案条件，以便继续递归下去
            return mid or left or right

        recurse_tree(root)
        return self.ans

# Iterative using parent pointers
class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        # 记录某个节点的父节点
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append((node.left))
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        # 记录p的所有上级节点
        while p:
            ancestors.add(p)
            p = parent[p]

        # 若q或q的任何上级节点不在p的上级节点集合中，说明p、q没有相交的祖先节点
        while q not in ancestors:
            q = parent[q]
        # 循环判断结束后，q要么已经赋值了p、q的第一个相交祖先节点（LCA），
        # 要么q一直向上到了root
        return q