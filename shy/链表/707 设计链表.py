
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head

        for _ in range(index + 1):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtIndex(self, index: int, val: int):
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        pred = self.head

        # 循环访问到index位置的前一个node，作为pred
        for _ in range(index):
            pred = pred.next

        to_add = ListNode(val)
        # 创建to_add指向下一个元素
        to_add.next = pred.next
        # 创建pred指向to——add
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return

        self.size -= 1
        pred = self.head

        for _ in range(index):
            pred = pred.next
        # 跳过要删除的node创建指向
        pred.next = pred.next.next









