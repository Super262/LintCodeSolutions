class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an integer
    """

    def backPackIII(self, a: list, v: list, m: int) -> int:
        n = len(a)
        dp = [[0] * (m + 1) for _ in range(2)]
        for i in range(1, n + 1):
            new_i = i % 2
            old_i = (i - 1) % 2
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[new_i][j] = max(dp[old_i][j], dp[new_i][j - a[i - 1]] + v[i - 1])
                else:
                    dp[new_i][j] = dp[old_i][j]
        return dp[n % 2][m]

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
