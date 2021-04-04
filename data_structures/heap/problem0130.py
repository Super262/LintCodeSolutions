class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, a: list) -> None:
        # 自底向上，从最后1个父节点到根节点
        if not a or len(a) < 2:
            return
        root_indices = []
        for i in range(len(a)):
            if 2 * i + 1 < len(a):
                root_indices.append(i)
        root_indices.reverse()
        for current_root in root_indices:
            while True:
                left_child = 2 * current_root + 1
                if left_child >= len(a):
                    break
                right_child = left_child
                if right_child < len(a) - 1:
                    right_child += 1
                if a[current_root] <= a[left_child] and a[current_root] <= a[right_child]:
                    break
                if a[left_child] <= a[right_child]:
                    a[current_root], a[left_child] = a[left_child], a[current_root]
                    current_root = left_child
                else:
                    a[current_root], a[right_child] = a[right_child], a[current_root]
                    current_root = right_child
