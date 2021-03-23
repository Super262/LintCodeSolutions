class Solution:

    def findMin(self, nums: list) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
