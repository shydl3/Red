'''
移除链表中 =val的所有节点
示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]
虽然输入的是列表，后台会自动转换为链表
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 直接方法
class Solution1:
    def removeElements(self, head, val:int):

        # 从初始head开始移除=val的节点
        while head and head.val == val:
            head = head.next

        # 如果移除后链表为空, return None
        if head is None:
            return head

        # 遍历节点，删除=val
        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head



# dummy node
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 定义一个在初始head node之前的dummy node，统一后续步骤
        dummy_node = ListNode(next=head)
        node = dummy_node

        # 如果后面还有节点
        while node.next:
            # =val则跳过
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy_node.next


# 递归
class Solution3:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        # 通过递归快速访问链表末尾节点，一步一步回退同时判断值
        head.next = self.removeElements(head.next, val)
        # 每层递归判断当前=val则跳过
        return head.next if head.val == val else head



