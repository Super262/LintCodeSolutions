class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root: TreeNode) -> TreeNode:
        import sys
        _, result, _ = self.helper(root, sys.maxsize)
        return result

    def helper(self, root: TreeNode, maxsize: int) -> tuple:
        if not root:
            return maxsize, None, 0
        left_minimum, left_min_tree, left_sum = self.helper(root.left, maxsize)
        right_minimum, right_min_tree, right_sum = self.helper(root.right, maxsize)
        root_sum = root.val + left_sum + right_sum
        min_sum = min(left_minimum, right_minimum, root_sum)
        if min_sum == left_minimum:
            return min_sum, left_min_tree, root_sum
        if min_sum == right_minimum:
            return min_sum, right_min_tree, root_sum
        return min_sum, root, root_sum
