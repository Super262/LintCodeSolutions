class Solution:

    def KthInArrays(self, arrays: list, k: int):
        import heapq
        # heapq 是一个 min-heap，所以所有数取相反数往里丢。取出来的时候要再取一个相反数
        if not arrays or k <= 0:
            return None
        sorted_arrays = []
        for arr in arrays:
            if not arr:
                continue
            sorted_arrays.append(sorted(arr, reverse=True))
        min_heap = []
        for index, array in enumerate(sorted_arrays):
            min_heap.append((-array[0], index, 0))
        heapq.heapify(min_heap)
        result = None
        for _ in range(k):
            num, array_index, item_index = heapq.heappop(min_heap)
            result = -num
            if item_index + 1 < len(sorted_arrays[array_index]):
                heapq.heappush(min_heap, (-sorted_arrays[array_index][item_index + 1], array_index, item_index + 1))
        return result
