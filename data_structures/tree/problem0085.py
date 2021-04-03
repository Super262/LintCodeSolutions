class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root: TreeNode, node: TreeNode) -> TreeNode:
        if not root:
            return node
        cur_node = root
        while True:
            if cur_node.val == node.val:
                break
            if cur_node.val > node.val:
                if not cur_node.left:
                    cur_node.left = node
                    break
                cur_node = cur_node.left
            else:
                if not cur_node.right:
                    cur_node.right = node
                    break
                cur_node = cur_node.right
        return root
