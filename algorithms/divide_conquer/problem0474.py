class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root: ParentTreeNode, a: ParentTreeNode, b: ParentTreeNode):
        if not root or not a or not b:
            return None
        if a == b:
            return a
        ancestors_path_a = []
        cur = a
        while cur:
            ancestors_path_a.append(cur)
            cur = cur.parent
        ancestors_path_b = []
        cur = b
        while cur:
            ancestors_path_b.append(cur)
            cur = cur.parent
        i = 1
        ancestors_path_a.reverse()
        ancestors_path_b.reverse()
        while i < len(ancestors_path_a) and i < len(ancestors_path_b):
            if ancestors_path_a[i] != ancestors_path_b[i]:
                break
            i += 1
        return ancestors_path_a[i - 1]
