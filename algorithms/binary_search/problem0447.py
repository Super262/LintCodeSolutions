class Solution:

    def searchBigSortedArray(self, reader, target: int) -> int:
        kth = 1
        while reader.get(kth - 1) < target:
            kth *= 2
        start = kth // 2
        end = kth - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
