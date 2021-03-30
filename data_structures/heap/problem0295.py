class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums: list) -> list:
        if not nums:
            return []
        result = [0] * len(nums)
        min_heap = []
        max_heap = []
        import heapq
        for i in range(len(nums)):
            if len(max_heap) == 0 or nums[i] <= -max_heap[0]:
                heapq.heappush(max_heap, -nums[i])
            else:
                heapq.heappush(min_heap, nums[i])
            self.balance(min_heap, max_heap)
            result[i] = -max_heap[0]
        return result

    def balance(self, min_heap: list, max_heap: list) -> None:
        import heapq
        while len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
