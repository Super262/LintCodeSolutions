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
        self.find_most_left(self.root)

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _next(self) -> TreeNode:
        cur_node = self.stack.pop()
        self.find_most_left(cur_node.right)
        return cur_node

    def find_most_left(self, cur_node: TreeNode):
        while cur_node:
            self.stack.append(cur_node)
            cur_node = cur_node.left
