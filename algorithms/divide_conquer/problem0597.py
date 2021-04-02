class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root: TreeNode) -> TreeNode:
        import sys
        _, _, _, result = self.helper(root, -sys.maxsize)
        return result

    def helper(self, root: TreeNode, minsize: int) -> tuple:
        if not root:
            return 0, 0, minsize, None
        left_nodes_count, left_values_sum, left_avg_max, left_max_tree = self.helper(root.left, minsize)
        right_nodes_count, right_values_sum, right_avg_max, right_max_tree = self.helper(root.right, minsize)
        root_nodes_count = 1 + right_nodes_count + left_nodes_count
        root_values_sum = root.val + right_values_sum + left_values_sum
        root_avg = root_values_sum / root_nodes_count
        root_avg_max = max(right_avg_max, left_avg_max, root_avg)
        if left_avg_max == root_avg_max:
            return root_nodes_count, root_values_sum, root_avg_max, left_max_tree
        if right_avg_max == root_avg_max:
            return root_nodes_count, root_values_sum, root_avg_max, right_max_tree
        return root_nodes_count, root_values_sum, root_avg_max, root
