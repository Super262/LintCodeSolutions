class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums: list) -> int:
        vote = 0
        result = -1
        for num in nums:
            if vote == 0:
                result = num
            if result == num:
                vote += 1
            else:
                vote -= 1
        return result
