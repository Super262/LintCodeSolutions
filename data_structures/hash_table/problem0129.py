class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, source_table: list) -> list:
        target_table = []
        for _ in range(len(source_table) * 2):
            target_table.append(None)
        for head in source_table:
            cur_node = head
            while cur_node:
                target_head_index = cur_node.val % len(target_table)
                if not target_table[target_head_index]:
                    target_table[target_head_index] = ListNode(cur_node.val)
                else:
                    cur_prev = target_table[target_head_index]
                    while cur_prev.next:
                        cur_prev = cur_prev.next
                    cur_prev.next = ListNode(cur_node.val)
                cur_node = cur_node.next
        return target_table
