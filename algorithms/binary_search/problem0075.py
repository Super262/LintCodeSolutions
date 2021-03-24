class Solution:

    def findPeak(self, A: list) -> int:
        if not A:
            return -1
        #  Range: [1:-2]
        start = 1
        end = len(A) - 2

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[mid + 1]:
                start = mid
            elif A[mid] < A[mid - 1]:
                end = mid
            else:
                return mid
        if A[start] > A[end]:
            return start
        else:
            # 这里使用else是因为有可能 start == end 成立
            return end
