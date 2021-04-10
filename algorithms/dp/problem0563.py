class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param m: An integer
    @return: An integer
    """

    def backPackV(self, nums: list, m: int) -> int:
        n = len(nums)
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(m, -1, -1):  # 对于求和运算，第1个有效值是0。因此，子集的和j从0开始计算，而不是1！
                if j < nums[i - 1]:
                    break
                dp[j] = dp[j] + dp[j - nums[i - 1]]
        return dp[m]
