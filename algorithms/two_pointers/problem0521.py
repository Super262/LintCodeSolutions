class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums: list) -> int:
        if not nums or len(nums) < 2:
            return len(nums)
        nums.sort()
        j = 1
        i = 0
        while i < len(nums):
            j = max(i + 1, j)
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j >= len(nums):
                break
            nums[i + 1] = nums[j]
            i += 1
        return i + 1
