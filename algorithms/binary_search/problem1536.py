class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """

    def searchRange(self, nums: list, target: int) -> list:
        if not nums:
            return [-1, -1]
        first_equal_or_larger_index = self.find_first_equal_or_larger(nums, 0, len(nums) - 1, target)
        if nums[first_equal_or_larger_index] != target:
            return [-1, -1]
        last_equal_or_larger_index = self.find_first_equal_or_larger(nums, 0, len(nums) - 1, target + 1) - 1
        return [first_equal_or_larger_index, last_equal_or_larger_index]

    def find_first_equal_or_larger(self, nums: list, start: int, end: int, target: int) -> int:
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        return end
