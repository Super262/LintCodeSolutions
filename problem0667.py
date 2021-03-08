class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        sLen = len(s)
        seqLen = [[0] * sLen for _ in range(sLen)]
        for i in range(sLen):
            seqLen[i][i] = 1
        # Note that we must iterate the string from its tail to its head to get
        # all elements for further steps.
        for start in reversed(range(0, sLen)):
            for end in range(start + 1, sLen):
                if s[start] == s[end]:
                    seqLen[start][end] = seqLen[start + 1][end - 1] + 2
                else:
                    seqLen[start][end] = max(seqLen[start][end - 1], seqLen[start + 1][end])
        return seqLen[0][sLen - 1]
