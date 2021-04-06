class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums: list) -> list:
        if not nums:
            return []
        prefix_sum_to_end = {}
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum == 0:
                return [0, i]
            if current_sum in prefix_sum_to_end:
                return [prefix_sum_to_end[current_sum] + 1, i]
            prefix_sum_to_end[current_sum] = i
        return []
