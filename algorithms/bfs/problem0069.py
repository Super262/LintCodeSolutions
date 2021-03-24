class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root: TreeNode) -> list:
        result = []
        if not root:
            return result
        import collections
        q = collections.deque([root])
        while q:
            level_values = []
            for _ in range(len(q)):
                node = q.popleft()
                level_values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_values)
        return result
