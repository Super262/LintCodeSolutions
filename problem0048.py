class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """

    def majorityNumber(self, nums, k):
        vote = [0] * (k - 1)
        candidate = [nums[0]] * (k - 1)
        nums_len = len(nums)
        for i in range(nums_len):
            is_matched = False
            for j in range(k - 1):
                if candidate[j] == nums[i]:
                    vote[j] += 1
                    is_matched = True
                    break
            if is_matched:
                continue
            for j in range(k - 1):
                if vote[j] == 0:
                    vote[j] = 1
                    candidate[j] = nums[i]
                    is_matched = True
                    break
            if is_matched:
                continue
            for j in range(k - 1):
                vote[j] -= 1
        for i in range(k - 1):
            vote[i] = 0
        for num in nums:
            for j in range(k - 1):
                if candidate[j] == num:
                    vote[j] += 1
                    break
        for i in range(k - 1):
            if vote[i] > nums_len // k:
                return candidate[i]
        return nums[0]
