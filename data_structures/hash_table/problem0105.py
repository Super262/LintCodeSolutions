class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head: RandomListNode) -> RandomListNode:
        old_to_new = {}
        cur_node = head
        while cur_node:
            old_to_new[cur_node] = RandomListNode(cur_node.label)
            cur_node = cur_node.next
        cur_node = head
        while cur_node:
            if cur_node.next:
                old_to_new[cur_node].next = old_to_new[cur_node.next]
            if cur_node.random:
                old_to_new[cur_node].random = old_to_new[cur_node.random]
            cur_node = cur_node.next
        return old_to_new[head]
