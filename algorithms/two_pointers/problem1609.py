class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the head node
    @return: the middle node
    """

    def middleNode(self, head: ListNode) -> ListNode:
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        return p_slow
