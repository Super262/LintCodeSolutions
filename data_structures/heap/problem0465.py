class Solution:

    def kthSmallestSum(self, a: list, b: list, k: int) -> int:
        if not a or not b or k <= 0 or k > len(a) * len(b):
            return 0
        h = len(a)
        w = len(b)
        used = []
        for _ in range(h):
            used.append([False] * w)
        min_heap = [(a[0] + b[0], 0, 0)]
        used[0][0] = True
        import heapq
        heapq.heapify(min_heap)
        for _ in range(k - 1):
            cur_num, index_a, index_b = heapq.heappop(min_heap)
            if index_a + 1 < h and not used[index_a + 1][index_b]:
                heapq.heappush(min_heap, (a[index_a + 1] + b[index_b], index_a + 1, index_b))
                used[index_a + 1][index_b] = True
            if index_b + 1 < w and not used[index_a][index_b + 1]:
                heapq.heappush(min_heap, (a[index_a] + b[index_b + 1], index_a, index_b + 1))
                used[index_a][index_b + 1] = True
        return min_heap[0][0]
