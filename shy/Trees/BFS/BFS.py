from collections import deque

class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def print_all_nodes(root: TreeNode):
    queue = deque([root])
    while queue:
        nodes_in_curr_level = len(queue)
        for _ in range(nodes_in_curr_level):
            node = queue.popleft()
            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)