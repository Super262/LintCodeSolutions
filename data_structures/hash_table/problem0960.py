class DataStream:
    class DLinkedNode:
        def __init__(self, value: int) -> None:
            self.next = None
            self.prev = None
            self.value = value

    def __init__(self):
        self.head = self.DLinkedNode(-1)
        self.tail = self.DLinkedNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.num_to_node = {}
        self.duplicated_nums = set()

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num: int) -> None:
        if num in self.duplicated_nums:
            return
        if num in self.num_to_node:
            current_node = self.num_to_node[num]
            self.remove_node(current_node)
            self.duplicated_nums.add(num)
            self.num_to_node.pop(num)
        else:
            current_node = self.DLinkedNode(num)
            self.push_back(current_node)
            self.num_to_node[num] = current_node

    """
    @return: the first unique number in stream
    """

    def firstUnique(self) -> int:
        return self.head.next.value

    def remove_node(self, current_node: DLinkedNode) -> None:
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        current_node.next = None
        current_node.prev = None

    def push_back(self, current_node: DLinkedNode) -> None:
        current_node.prev = self.tail.prev
        current_node.next = self.tail
        current_node.prev.next = current_node
        self.tail.prev = current_node
