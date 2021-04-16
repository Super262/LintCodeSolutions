class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums: list, k: int) -> list:
        if not nums or len(nums) < k:
            return []
        answer = [0] * (len(nums) - k + 1)
        ans_top = 0
        for i in range(k):
            answer[ans_top] += nums[i]
        ans_top += 1
        right = k
        left = 0
        while right < len(nums):
            answer[ans_top] = answer[ans_top - 1] + nums[right] - nums[left]
            left += 1
            right += 1
            ans_top += 1
        return answer
