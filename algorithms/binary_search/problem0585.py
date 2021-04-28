class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums: list) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if mid + 1 <= end and nums[mid + 1] > nums[mid]:
                start = mid + 1
                continue
            if mid - 1 >= start and nums[mid - 1] > nums[mid]:
                end = mid - 1
                continue
            return nums[mid]
        return nums[start]
