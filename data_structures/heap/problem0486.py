class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays: list) -> list:
        import heapq
        candidates_pool = []
        for i in range(len(arrays)):
            if (len(arrays[i])) == 0:
                continue
            candidates_pool.append((arrays[i][0], i, 0))
        heapq.heapify(candidates_pool)
        result = []
        while candidates_pool:
            val, y, x = heapq.heappop(candidates_pool)
            if x + 1 < len(arrays[y]):
                heapq.heappush(candidates_pool, (arrays[y][x + 1], y, x + 1))
            result.append(val)
        return result
