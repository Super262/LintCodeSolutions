class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        return self.get_height(root)[0]

    def get_height(self, root: TreeNode) -> tuple:
        if not root:
            return True, 0
        root_height = 1
        left_balanced, left_height = self.get_height(root.left)
        right_balanced, right_height = self.get_height(root.right)
        root_height += max(left_height, right_height)
        return left_balanced and right_balanced and abs(right_height - left_height) < 2, root_height
