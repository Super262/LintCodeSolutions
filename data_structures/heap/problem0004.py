class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = {1}
        cur_val = 0
        import heapq
        for i in range(n):
            cur_val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                next_val = cur_val * factor
                if next_val in visited:
                    continue
                heapq.heappush(heap, next_val)
                visited.add(next_val)
        return cur_val
