class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """

    def findMin(self, nums: list) -> int:
        sum_of_nums = sum(nums)
        m = sum_of_nums // 2
        n = len(nums)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, -1, -1):
                if j < nums[i - 1]:
                    break
                dp[j] = max(dp[j - nums[i - 1]] + nums[i - 1], dp[j])
        return sum_of_nums - 2 * dp[m]
