class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums: list, s: int) -> int:
        if not nums:
            return -1
        left = 0
        right = 0
        min_len = -1
        current_sum = 0
        while right < len(nums):
            current_sum += nums[right]
            while left <= right and current_sum >= s:
                if min_len <= 0 or right - left + 1 < min_len:
                    min_len = right - left + 1
                current_sum -= nums[left]
                left += 1
            right += 1
        return min_len
