class Solution:

    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        if not A or not B or not C or not D:
            return 0
        sum_ab = {}
        for a in A:
            for b in B:
                sum_ab[a + b] = sum_ab.get(a + b, 0) + 1
        result = 0
        for c in C:
            for d in D:
                result += sum_ab.get(-c - d, 0)
        return result
