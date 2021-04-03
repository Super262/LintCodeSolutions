class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root: TreeNode) -> None:
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, root: TreeNode):
        if not root:
            return None
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        return right_last or left_last or root
