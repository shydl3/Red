'''
给定一个链表的头节点  head ，
返回链表开始入环的第一个节点。
如果链表无环，则返回 null。
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 简单集合
class Solution1:
    def detectCycle(self, head):
        visited = set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None


# 快慢指针
class Solution2:
    def detectCycle(self, head: ListNode):
        slow = head
        fast = head

        while fast and fast.next:
            # 慢指针移动1
            slow = slow.next
            # 快指针移动2
            fast = fast.next.next

            # 两个指针相遇时，说明有环，但相遇的位置不一定是环的入口
            # 重制慢指针，同时移动1，再次相遇时就是环的入口
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        # 如果fast空了，说明没有环
        return None

