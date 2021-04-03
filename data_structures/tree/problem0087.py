class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return root
        if root.val == target:
            if not root.left and not root.right:
                root = None
            elif root.left and root.right:
                root.val = self.find_max(root.left)
                root.left = self.removeNode(root.left, root.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
        elif root.val > target:
            root.left = self.removeNode(root.left, target)
        else:
            root.right = self.removeNode(root.right, target)
        return root

    def find_max(self, root: TreeNode) -> int:
        if not root.right:
            return root.val
        return self.find_max(root.right)
