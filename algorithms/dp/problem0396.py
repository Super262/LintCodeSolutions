class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values: list) -> bool:
        if not values:
            return True
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = values[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(values[i] - dp[i + 1][j], values[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0
