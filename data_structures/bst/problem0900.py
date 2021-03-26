class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root: TreeNode, target: float) -> int:
        upper = root
        lower = root
        while root:
            if root.val > target:
                upper = root
                root = root.left
            elif root.val < target:
                lower = root
                root = root.right
            else:
                return root.val
        # 注意 upper.val 不一定比 target 大；lower.val 不一定比 target 小
        if abs(upper.val - target) < abs(target - lower.val):
            return upper.val
        else:
            return lower.val
