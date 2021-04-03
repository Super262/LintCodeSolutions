class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root: TreeNode, target: float, k: int) -> list:
        result = []
        if not root:
            return result
        lower_stack = self.initialize_stack(root, target)
        upper_stack = list(lower_stack)
        if target < float(lower_stack[-1].val):
            self.move_lower(lower_stack)
        else:
            self.move_upper(upper_stack)
        for _ in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
        return result

    def is_lower_closer(self, lower_stack: list, upper_stack: list, target: float):
        if not lower_stack:
            return False
        if not upper_stack:
            return True
        return abs(float(lower_stack[-1].val) - target) < abs(float(upper_stack[-1].val - target))

    def initialize_stack(self, root: TreeNode, target: float) -> list:
        stack = []
        while root:
            stack.append(root)
            if float(root.val) > target:
                root = root.left
            else:
                root = root.right
        return stack

    def move_upper(self, stack: list) -> None:
        node = stack[-1]
        if not node.right:
            node = stack.pop()
            while len(stack) > 0 and stack[-1].right == node:
                node = stack.pop()
            return
        node = node.right
        while node:
            stack.append(node)
            node = node.left

    def move_lower(self, stack: list) -> None:
        node = stack[-1]
        if not node.left:
            node = stack.pop()
            while len(stack) > 0 and stack[-1].left == node:
                node = stack.pop()
            return
        node = node.left
        while node:
            stack.append(node)
            node = node.right
