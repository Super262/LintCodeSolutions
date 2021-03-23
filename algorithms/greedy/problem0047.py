class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """

    def majorityNumber(self, nums: list) -> int:
        vote1 = 0
        vote2 = 0
        candidate1 = nums[0]
        candidate2 = nums[0]
        nums_len = len(nums)
        for i in range(nums_len):
            if candidate1 == nums[i]:
                vote1 += 1
                continue
            if candidate2 == nums[i]:
                vote2 += 1
                continue
            if vote1 == 0:
                candidate1 = nums[i]
                vote1 = 1
                continue
            if vote2 == 0:
                candidate2 = nums[i]
                vote2 = 1
                continue
            vote1 -= 1
            vote2 -= 1
        vote1 = 0
        vote2 = 0
        for num in nums:
            if num == candidate1:
                vote1 += 1
            elif num == candidate2:
                vote2 += 1
        if vote1 > nums_len // 3:
            return candidate1
        else:
            return candidate2
