'''
Problem: 移除链表元素
Source: https://leetcode-cn.com/problems/remove-linked-list-elements/

题意：删除链表中等于给定值 val 的所有节点。

示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]

示例 2： 输入：head = [], val = 1 输出：[]

示例 3： 输入：head = [7,7,7,7], val = 7 输出：[]
'''

from typing import Optional

class ListNode: # 链表结构
    def _init_(self, val = 0, next = None): # 初始化
        self.val = val # 节点值
        self.next = next   # 下一节点

class Solution:
    def removeElements(self, head: Optional[ListNode], val:int): # optinal表示可选参数
        dummy_Head = ListNode(next = head) # 创建虚拟头节点

        cur = dummy_Head

        while cur.next: # 当前节点的下一个节点存在
            if cur.next.val == val: # 当前节点的下一个节点的值等于val
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_Head.next