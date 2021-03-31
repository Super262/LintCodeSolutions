class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> list:
        results = []
        if not root:
            return results
        self.get_paths(root, [str(root.val)], results)
        return results

    def get_paths(self, root: TreeNode, prefix: list, output: list) -> None:
        if not root:
            return
        if not root.left and not root.right:
            output.append("->".join(prefix))
            return
        if root.left:
            prefix.append(str(root.left.val))
            self.get_paths(root.left, prefix, output)
            prefix.pop()
        if root.right:
            prefix.append(str(root.right.val))
            self.get_paths(root.right, prefix, output)
            prefix.pop()
