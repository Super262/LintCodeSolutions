class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums: list, target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
