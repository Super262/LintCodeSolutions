class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums: list) -> int:
        vote = 0
        result = nums[0]
        for num in nums:
            if result == num:
                vote += 1
                continue
            if vote == 0:
                result = num
                vote = 1
                continue
            vote -= 1
        return result
