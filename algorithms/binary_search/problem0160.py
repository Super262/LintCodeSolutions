class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums: list) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # 选择最后一个值nums[end]为"标杆"，以应对特殊情况：正常的排序数组
            if nums[mid] == nums[end]:
                end -= 1
            elif nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])
