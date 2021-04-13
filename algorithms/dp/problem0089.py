class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    # 滚动数组优化
    def kSum(self, a: list, k: int, target: int) -> int:
        n = len(a)
        dp = [[[0] * (target + 1) for _ in range(k + 1)] for _ in range(2)]
        dp[0][0][0] = 1  # Don't forget initialization!
        for i in range(1, n + 1):
            new_i = i % 2
            old_i = (i - 1) % 2
            dp[new_i][0][0] = 1
            for j in range(1, k + 1):
                for s in range(1, target + 1):
                    dp[new_i][j][s] = dp[old_i][j][s]
                    if s >= a[i - 1]:
                        dp[new_i][j][s] += dp[old_i][j - 1][s - a[i - 1]]
        return dp[n % 2][k][target]
