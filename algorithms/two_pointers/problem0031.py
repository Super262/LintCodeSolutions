class Solution:

    def partitionArray(self, nums: list, k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            # 快速排序的边界不包含"等于"的情况，这里是"非左即右"！
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left
