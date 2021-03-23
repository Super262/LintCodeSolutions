class Solution:

    def kthSmallest(self, matrix: list, k: int):
        if not matrix or not matrix[0] or k <= 0:
            return None
        h = len(matrix)
        w = len(matrix[0])
        used = []
        for _ in range(h):
            used.append([False] * w)
        min_heap = [(matrix[0][0], 0, 0)]
        used[0][0] = True
        import heapq
        heapq.heapify(min_heap)
        for i in range(k - 1):
            num, y, x = heapq.heappop(min_heap)
            if y + 1 < h and not used[y + 1][x]:
                heapq.heappush(min_heap, (matrix[y + 1][x], y + 1, x))
                used[y + 1][x] = True
            if x + 1 < w and not used[y][x + 1]:
                heapq.heappush(min_heap, (matrix[y][x + 1], y, x + 1))
                used[y][x + 1] = True
        return min_heap[0][0]
