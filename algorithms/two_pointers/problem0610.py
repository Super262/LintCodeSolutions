class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """

    def twoSum7(self, nums: list, target: int) -> list:
        if not nums or len(nums) < 2:
            return [-1, -1]
        target = abs(target)
        j = 1
        for i in range(0, len(nums)):
            j = max(j, i + 1)
            while j < len(nums) and nums[j] - nums[i] < target:
                j += 1
            if j >= len(nums):
                break
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
        return [-1, -1]
