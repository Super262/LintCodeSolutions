class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


"""
Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:

    def __init__(self, root: TreeNode) -> None:
        self.root = root
        self.stack = []
        cur_node = self.root
        while cur_node:
            self.stack.append(cur_node)
            cur_node = cur_node.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _next(self) -> TreeNode:
        cur_node = self.stack.pop()
        cur_next = cur_node.right
        while cur_next:
            self.stack.append(cur_next)
            cur_next = cur_next.left
        return cur_node
