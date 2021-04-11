class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        f = [0] * (n + 1)
        f[0] = 1
        if s[0] != "0":
            f[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                f[i] += f[i - 1]
            if s[i - 2] != "0" and 10 <= int(s[i - 2: i]) <= 26:
                f[i] += f[i - 2]
        return f[n]
