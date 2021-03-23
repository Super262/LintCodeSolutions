class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums: list, target: int) -> int:
        result = 0
        nums.sort()
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            else:
                result += end - start
                start += 1
        return result
