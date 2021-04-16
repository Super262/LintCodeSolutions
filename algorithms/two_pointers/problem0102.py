class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast_p = head.next
        slow_p = head
        while fast_p != slow_p:
            if not fast_p or not fast_p.next:
                return False
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        return True
