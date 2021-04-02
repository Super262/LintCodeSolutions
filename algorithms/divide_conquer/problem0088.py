class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # 题解：递归查找A和B， 找到A和B第一次在同一棵子树中的子树根节点即是LCA。
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root: TreeNode, a: TreeNode, b: TreeNode):
        if not root or not a or not b:
            return None
        if root == a or root == b:
            return root
        left_result = self.lowestCommonAncestor(root.left, a, b)
        right_result = self.lowestCommonAncestor(root.right, a, b)
        if left_result and right_result:
            return root
        if left_result:
            return left_result
        if right_result:
            return right_result
        return None
