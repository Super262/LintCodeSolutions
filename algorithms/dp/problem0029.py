class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s_len_1 = len(s1)
        s_len_2 = len(s2)
        if s_len_1 + s_len_2 != len(s3):
            return False
        dp = [[False] * (s_len_2 + 1) for _ in range(2)]
        dp[0][0] = True
        for l in range(1, s_len_2 + 1):
            if s2[l - 1] != s3[l - 1]:
                break
            dp[0][l] = dp[0][l - 1]
        for l1 in range(1, s_len_1 + 1):
            old_l1 = (l1 - 1) % 2
            new_l1 = l1 % 2
            dp[new_l1][0] = dp[old_l1][0] and s3[l1 - 1] == s1[l1 - 1]
            for l2 in range(1, s_len_2 + 1):
                dp[new_l1][l2] = (s1[l1 - 1] == s3[l1 + l2 - 1] and dp[old_l1][l2]) or (
                        s2[l2 - 1] == s3[l1 + l2 - 1] and dp[new_l1][l2 - 1])
        return dp[s_len_1 % 2][s_len_2]
