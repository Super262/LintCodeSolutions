class Solution:

    def findMedianSortedArrays(self, A: list, B: list) -> float:
        n = len(A) + len(B)
        if n % 2 == 0:
            return (self.find_kth(A, B, n // 2) + self.find_kth(A, B, n // 2 + 1)) / 2.0
        else:
            return self.find_kth(A, B, n // 2 + 1)

    def find_kth(self, a: list, b: list, k: int) -> int:
        if len(a) == 0:
            return b[k - 1]
        if len(b) == 0:
            return a[k - 1]
        min_val = min(a[0], b[0])
        max_val = max(a[-1], b[-1])
        while min_val + 1 < max_val:
            mid_val = min_val + (max_val - min_val) // 2
            if self.count_less_or_equal(a, mid_val) + self.count_less_or_equal(b, mid_val) >= k:
                max_val = mid_val
            else:
                min_val = mid_val
        if self.count_less_or_equal(a, min_val) + self.count_less_or_equal(b, min_val) >= k:
            return min_val
        return max_val

    def count_less_or_equal(self, arr: list, target: int) -> int:
        start = 0
        end = len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] > target:
                end = mid
            else:
                start = mid
        if arr[start] > target:
            return start
        if arr[end] > target:
            return end
        return len(arr)
