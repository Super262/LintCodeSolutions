class Solution:

    def moveZeroes(self, nums: list) -> None:
        # Minimize the total number of operations!
        if not nums:
            return
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
