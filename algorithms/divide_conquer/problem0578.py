class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root: TreeNode, a: TreeNode, b: TreeNode):
        a_existed, b_existed, lca = self.helper(root, a, b)
        if a_existed and b_existed:
            return lca
        return None

    def helper(self, root: TreeNode, a: TreeNode, b: TreeNode) -> tuple:
        if not root or not a or not b:
            return False, False, None
        a_existed_left, b_existed_left, left_node = self.helper(root.left, a, b)
        a_existed_right, b_existed_right, right_node = self.helper(root.right, a, b)
        a_existed_root = a_existed_left or a_existed_right or root == a
        b_existed_root = b_existed_left or b_existed_right or root == b
        if root == a or root == b:
            return a_existed_root, b_existed_root, root
        if left_node is not None and right_node is not None:
            return a_existed_root, b_existed_root, root
        if left_node is not None:
            return a_existed_root, b_existed_root, left_node
        if right_node is not None:
            return a_existed_root, b_existed_root, right_node
        return False, False, None
