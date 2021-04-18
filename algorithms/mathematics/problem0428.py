class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x: float, n: int) -> float:
        is_neg_pow = False
        if n < 0:
            is_neg_pow = True
            n = -n
        result = 1.0
        while n > 0:
            if n & 1 != 0:
                result *= x
            x *= x
            n >>= 1
        if is_neg_pow:
            result = 1 / result
        return result
