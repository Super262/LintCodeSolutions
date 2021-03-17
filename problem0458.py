class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums: list, target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
