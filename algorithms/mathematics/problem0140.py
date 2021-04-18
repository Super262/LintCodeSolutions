class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    # 迭代法会超时，暂时不知道为什么！
    def fastPower(self, a: int, b: int, n: int) -> int:
        if n == 0:
            return 1 % b
        product = self.fastPower(a, b, n // 2)
        product = (product * product) % b
        if n % 2 == 1:
            product = product * a % b
        return product
