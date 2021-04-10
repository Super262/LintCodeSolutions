class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an integer
    """

    def backPackIII(self, a: list, v: list, m: int) -> int:
        n = len(a)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - a[i - 1]] + v[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]

# 优化后的多重背包
# class Solution:
#
#     def backPackIII(self, A, V, m):
#         n = len(A)
#         dp = [0] * (m + 1)
#
#         for i in range(n):
#             for j in range(A[i], m + 1):
#                 dp[j] = max(dp[j], dp[j - A[i]] + V[i])
#
#         return dp[m]
