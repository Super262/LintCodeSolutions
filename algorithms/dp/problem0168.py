class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums: list) -> int:
        if not nums:
            return 0
        values = [0] * (len(nums) + 2)
        n = len(values)
        for i in range(1, n - 1):
            values[i] = nums[i - 1]
        values[0] = 1
        values[-1] = 1
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            dp[i][i + 1] = 0
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = 0
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + values[i] * values[k] * values[j] + dp[k][j])
        return dp[0][n - 1]
