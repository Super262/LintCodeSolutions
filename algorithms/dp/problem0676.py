class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """

    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        n = len(s)
        max_bound = 1000000007
        f0 = 1
        f1 = self.count_one(s, 0) * f0
        for i in range(2, n + 1):
            f2 = self.count_one(s, i - 1) * f1 % max_bound + self.count_two(s, i - 2) * f0 % max_bound
            f2 %= max_bound
            f0 = f1
            f1 = f2
        return f1

    def count_one(self, s: str, start: int) -> int:
        if s[start] == "*":
            return 9
        if s[start] == "0":
            return 0
        return 1

    def count_two(self, s: str, start: int) -> int:
        if s[start] == "0":
            return 0
        elif s[start] == "1":
            if s[start + 1] == "*":
                return 9
            else:
                return 1
        elif s[start] == "2":
            if s[start + 1] == "*":
                return 6
            elif 0 <= int(s[start + 1]) <= 6:
                return 1
            else:
                return 0
        elif s[start] == "*":
            if s[start + 1] == "*":
                return 15
            elif 0 <= int(s[start + 1]) <= 6:
                return 2
            else:
                return 1
        else:
            return 0
