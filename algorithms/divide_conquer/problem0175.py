class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root: TreeNode) -> None:
        self.helper(root)

    def helper(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left_inverted = self.helper(root.left)
        right_inverted = self.helper(root.right)
        root.right = left_inverted
        root.left = right_inverted
        return root
