class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        f0 = 1
        f1 = 0
        if s[0] != "0":
            f1 = 1
        f2 = 0
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                f2 += f1
            if s[i - 2] != "0" and 10 <= int(s[i - 2: i]) <= 26:
                f2 += f0
            f0 = f1
            f1 = f2
            f2 = 0
        return f1
