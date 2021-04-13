class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """

    def subarraySumII(self, a: list, start: int, end: int) -> int:
        prefix_sum = [0] * (len(a) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
        result = 0
        left = 0
        right = 0
        for i in range(1, len(prefix_sum)):
            while left < i and prefix_sum[i] - prefix_sum[left] > end:
                left += 1
            while right < i and prefix_sum[i] - prefix_sum[right] >= start:  # ">=" 保证循环结束后，right是第1个不满足要求的位置
                right += 1
            result += right - left
        return result
