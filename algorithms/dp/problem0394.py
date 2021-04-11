class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True
        for i in range(2, n + 1):
            dp[i] = not dp[i - 1] or not dp[i - 2]
        return dp[n]
