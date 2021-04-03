class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root: TreeNode, k: int):
        if not root:
            return None
        stack = []
        cur_node = root
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
        for _ in range(k - 1):
            cur_node = stack[-1]
            if cur_node.right:
                cur_node = cur_node.right
                while cur_node:
                    stack.append(cur_node)
                    cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                while stack and stack[-1].right == cur_node:
                    cur_node = stack.pop()  # 弹出比自己小的（失效的）节点
        return stack[-1].val
