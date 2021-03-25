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
        result = 2147483647
        if not root:
            return result
        stack = []
        dis = 2147483647
        self.find_most_left(stack, root)
        while self.has_next(stack):
            cur_val = self.next_val(stack)
            if abs(cur_val - target) < dis:
                result = cur_val
                dis = abs(cur_val - target)
        return result

    def has_next(self, stack: list) -> bool:
        return len(stack) > 0

    def next_val(self, stack: list) -> int:
        node = stack.pop()
        self.find_most_left(stack, node.right)
        return node.val

    def find_most_left(self, stack: list, root: TreeNode) -> None:
        while root:
            stack.append(root)
            root = root.left
