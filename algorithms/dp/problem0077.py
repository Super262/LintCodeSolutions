class Solution:
    """
    @param a: A string
    @param b: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, a: str, b: str) -> int:
        if not a or not b:
            return 0
        l1 = len(a)
        l2 = len(b)
        dp = [[0] * (l2 + 1) for _ in range(2)]
        for i in range(1, l1 + 1):
            new_i = i % 2
            old_i = (i - 1) % 2
            for j in range(1, l2 + 1):
                if a[i - 1] == b[j - 1]:
                    dp[new_i][j] = dp[old_i][j - 1] + 1
                else:
                    dp[new_i][j] = max(dp[old_i][j], dp[new_i][j - 1])
        return dp[l1 % 2][l2]
