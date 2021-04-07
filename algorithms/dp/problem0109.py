class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle: list) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        dp = [[0] * i for i in range(1, n + 1)]
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]
