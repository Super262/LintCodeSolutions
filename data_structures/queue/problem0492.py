class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item: int) -> None:
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def dequeue(self) -> int:
        popped_value = self.head.val
        self.head = self.head.next
        return popped_value


class Node:

    def __init__(self, _val):
        self.next = None
        self.val = _val
