'''
两个单链表的头节点 headA 和 headB ，
请你找出并返回两个单链表相交的起始节点。
如果两个链表没有交点，返回 null

这里的链表不存在环
'''


#6
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA





