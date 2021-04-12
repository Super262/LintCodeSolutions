class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    # 滚动数组优化
    def backPack(self, m: int, a: list) -> int:
        n = len(a)
        dp = [[False] * (m + 1) for _ in range(2)]
        dp[0][0] = True
        for i in range(1, n + 1):
            new_i = i % 2
            old_i = (i - 1) % 2
            dp[new_i][0] = True
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[new_i][j] = dp[old_i][j] or dp[old_i][j - a[i - 1]]
                else:
                    dp[new_i][j] = dp[old_i][j]
        n_reduced = n % 2
        for w in range(m, -1, -1):
            if dp[n_reduced][w]:
                return w
        return -1
