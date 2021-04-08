class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings: list) -> list:
        if not buildings:
            return []

        class MaxHeap:

            def __init__(self):
                self.removed_keys = set()
                self.data = []

            def push(self, unique_key: int, value: int) -> None:
                import heapq
                heapq.heappush(self.data, (-value, unique_key))

            def pop(self) -> tuple:
                if not self.data:
                    return 0, None
                import heapq
                value, unique_key = heapq.heappop(self.data)
                self.prune()
                return -value, unique_key

            def peek(self) -> tuple:
                if not self.data:
                    return 0, None
                value, unique_key = self.data[0]
                return -value, unique_key

            def remove(self, unique_key: int) -> None:
                self.removed_keys.add(unique_key)
                self.prune()

            def prune(self) -> None:
                # 延迟删除
                import heapq
                while self.data and self.data[0][1] in self.removed_keys:
                    heapq.heappop(self.data)

        points = []
        for key, building in enumerate(buildings):
            start, end, height = building
            points.append((start, False, height, key))
            points.append((end, True, height, key))
        points.sort()
        temp_outline = []
        max_heap = MaxHeap()
        for p in points:
            p_x, is_end, height, p_id = p
            if is_end:
                max_heap.remove(p_id)
            else:
                max_heap.push(p_id, height)
            current_max_height = max_heap.peek()[0]
            if not temp_outline:
                temp_outline.append([p_x, p_x, current_max_height])
            elif temp_outline[-1][0] == p_x:
                temp_outline[-1][2] = max(current_max_height, temp_outline[-1][2])  # 考虑两个矩形重叠的情况
            elif temp_outline[-1][2] != current_max_height:
                temp_outline[-1][1] = p_x
                temp_outline.append([p_x, p_x, current_max_height])  # 这个语句块不能和第一个if语句块合并
        outline = []
        for item in temp_outline:
            if item[-1] == 0:
                continue
            outline.append(item)
        return outline
