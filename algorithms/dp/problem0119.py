class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        word_len_1 = len(word1)
        word_len_2 = len(word2)
        dp = [[0] * (word_len_2 + 1) for _ in range(2)]
        for l in range(1, word_len_2 + 1):
            dp[0][l] = l
        for l1 in range(1, word_len_1 + 1):
            new_l1 = l1 % 2
            old_l1 = (l1 - 1) % 2
            dp[new_l1][0] = l1
            for l2 in range(1, word_len_2 + 1):
                if word1[l1 - 1] == word2[l2 - 1]:
                    dp[new_l1][l2] = min(dp[old_l1][l2 - 1], dp[new_l1][l2 - 1] + 1, dp[old_l1][l2] + 1)
                else:
                    dp[new_l1][l2] = min(dp[old_l1][l2 - 1], dp[new_l1][l2 - 1], dp[old_l1][l2]) + 1
        return dp[word_len_1 % 2][word_len_2]
