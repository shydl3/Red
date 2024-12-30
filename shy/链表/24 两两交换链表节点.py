'''
两两交换链表相邻节点，返回结果的头节点
必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换
'''

# 递归
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        ptr1 = head
        ptr2 = head.next
        next = head.next.next

        ptr2.next = ptr1
        ptr1.next = self.swapPairs(next)

        return ptr2


