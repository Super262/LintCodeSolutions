class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root: TreeNode, k1: int, k2: int) -> list:
        result = []
        self.helper(root, k1, k2, result)
        result.sort()
        return result

    def helper(self, root: TreeNode, k1: int, k2: int, result: list) -> None:
        if not root or k1 > k2:
            return
        if k1 <= root.val <= k2:
            result.append(root.val)
            self.helper(root.left, k1, root.val, result)
            self.helper(root.right, root.val, k2, result)
        elif root.val > k2:
            self.helper(root.left, k1, k2, result)
        else:
            self.helper(root.right, k1, k2, result)
