class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root: TreeNode, a: TreeNode, b: TreeNode):
        if not root or not a or not b:
            return None
        path_a = []
        if not self.find_path(root, a, path_a):
            return None
        path_b = []
        if not self.find_path(root, b, path_b):
            return None
        i = 1
        while i < len(path_a) and i < len(path_b):
            if path_a[i] != path_b[i]:
                break
            i += 1
        return path_a[i - 1]

    def find_path(self, root: TreeNode, target: TreeNode, path: list) -> bool:
        if not root or not target:
            return False
        path.append(root)
        if root == target:
            return True
        if self.find_path(root.left, target, path) or self.find_path(root.right, target, path):
            return True
        path.pop()
        return False
