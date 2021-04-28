class Solution:

    def findMin(self, nums: list) -> int:
        # 输入数据限制：无重复值
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        # 选择最后一个值为"标杆"，以应对特殊情况：正常的排序数组
        target = nums[-1]

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
