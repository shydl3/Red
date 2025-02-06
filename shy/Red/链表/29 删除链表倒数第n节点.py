'''
删除链表的倒数第 n 个结点，
并且返回链表的头结点
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):

        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy_head = ListNode(0, head)
        length = getLength(head)
        cur = dummy_head

        # 倒数第n个节点，注意循环范围。
        # 循环访问到 目标位置 前一个节点
        for i in range(1, length - n + 1):
            cur = cur.next

        # 跳过要删除的节点
        cur.next = cur.next.next

        # return 真正的head
        return dummy_head.next







