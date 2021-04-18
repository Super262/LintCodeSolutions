class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a: int, b: int, n: int) -> int:
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * a % b
            a = a * a % b  # 一定要对b取余，否则会超时
            n >>= 1
        return ans % b
