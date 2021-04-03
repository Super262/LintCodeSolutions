class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root: TreeNode) -> bool:
        import sys
        return self.helper(root, -sys.maxsize, sys.maxsize)

    def helper(self, root: TreeNode, lower_bound: int, upper_bound: int) -> bool:
        if not root:
            return True
        if root and (root.val <= lower_bound or root.val >= upper_bound):
            return False
        return self.helper(root.left, lower_bound, root.val) and self.helper(root.right, root.val, upper_bound)
