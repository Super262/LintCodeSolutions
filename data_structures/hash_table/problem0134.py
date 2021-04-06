class DLinkedNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


def remove_node(node: DLinkedNode) -> DLinkedNode:
    node.next.prev = node.prev
    node.prev.next_val = node.next
    node.prev = None
    node.next = None
    return node


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.data = {}
        self.capacity = capacity
        self.head = DLinkedNode(-1, -1)
        self.tail = DLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_left(self, node: DLinkedNode):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def pop_right(self) -> DLinkedNode:
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next_val = self.tail
        return node

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key: int) -> int:
        if key in self.data:
            node = remove_node(self.data[key])
            self.add_left(node)
            self.data[key] = self.head.next
            return self.head.next.value
        else:
            return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key: int, value: int) -> None:
        if key in self.data:
            node = remove_node(self.data[key])
            node.value = value
        else:
            if len(self.data) == self.capacity:
                self.data.pop(self.pop_right().key)
            node = DLinkedNode(key, value)
        self.add_left(node)
        self.data[key] = self.head.next
