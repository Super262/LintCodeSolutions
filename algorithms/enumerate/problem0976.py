class Solution:

    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        if not A or not B or not C or not D:
            return 0
        sum_ab = {}
        for a in A:
            for b in B:
                if a + b in sum_ab:
                    sum_ab[a + b] += 1
                else:
                    sum_ab[a + b] = 1
        result = 0
        for c in C:
            for d in D:
                if -c - d in sum_ab:
                    result += sum_ab[-c - d]
        return result
