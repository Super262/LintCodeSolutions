class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(2)]   # 滚动数组，空间优化
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i % 2][j] = dp[i % 2][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + grid[i][j]
                else:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1]) + grid[i][j]
        return dp[(m - 1) % 2][n - 1]
