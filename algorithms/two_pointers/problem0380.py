class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode):
        if head_a is None or head_b is None:
            return None
        p1 = head_a
        p2 = head_b
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
            if p1 is None and p2 is None:
                return None
            if p1 is None:
                p1 = head_b
            if p2 is None:
                p2 = head_a
        return p1
