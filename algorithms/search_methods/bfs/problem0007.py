class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        queue = [root]
        i = 0
        while i < len(queue):
            if queue[i]:
                queue.append(queue[i].left)
                queue.append(queue[i].right)
            i += 1
        while queue and not queue[-1]:
            queue.pop()
        result = []
        for node in queue:
            if node:
                result.append(str(node.val))
            else:
                result.append("#")
        return ",".join(result)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data: str):
        if not data:
            return None
        node_values = data.split(",")
        root = TreeNode(node_values[0])
        queue = [root]
        is_left_child = True
        i = 0
        for val in node_values[1:]:
            if val != "#":
                child = TreeNode(int(val))
                if is_left_child:
                    queue[i].left = child
                else:
                    queue[i].right = child
                queue.append(child)
            if not is_left_child:
                i += 1
            is_left_child = not is_left_child
        return root
