class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    # 滚动数组优化
    def backPackII(self, m: int, a: list, v: list) -> int:
        n = len(a)
        dp = [[0] * (m + 1) for _ in range(2)]
        for i in range(1, n + 1):
            new_i = i % 2
            old_i = (i - 1) % 2
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[new_i][j] = max(dp[old_i][j], dp[old_i][j - a[i - 1]] + v[i - 1])
                else:
                    dp[new_i][j] = dp[old_i][j]
        return dp[n % 2][m]
