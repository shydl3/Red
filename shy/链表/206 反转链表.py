'''
反转一个单链表。
示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
'''
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

# 双指针
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        # 首、尾节点
        left, right = head, None
        # 从第一个节点开始：
        while left:
            # 暂存下一个节点
            next = left.next
            # 下一个指向最右边节点
            left.next = right
            right = left
            left = next
        return right

# 递归
class Solution2:
    def reverseList(self, head: ListNode):

        def recur(left, right):
            if not left:
                return right
            # 通过递归返回最后链表的末尾节点
            tail_node = recur(left.next, left)
            # 递归函数传值是逆序，所以调转方向
            left.next = right
            
            return tail_node

        return recur(head, None)




