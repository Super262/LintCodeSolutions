class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def __init__(self):
        self.max_sum = 0
        self.result = None

    def findSubtree(self, root) -> TreeNode:
        self.helper(root)
        return self.result

    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        root_sum = self.helper(root.left) + self.helper(root.right) + root.val
        if root_sum > self.max_sum:
            self.max_sum = root_sum
            self.result = root
        return root_sum
