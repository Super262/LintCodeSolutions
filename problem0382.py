class Solution:

    def triangleCount(self, S: list) -> int:
        result = 0
        if len(S) < 3:
            return result
        S.sort()
        c = 2
        while c < len(S):
            a = 0
            b = c - 1
            while a < b:
                if S[a] + S[b] > S[c]:
                    result += b - a
                    b -= 1
                else:
                    a += 1
            c += 1
        return result
