class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """

    def gcd(self, a: int, b: int) -> int:
        big = max(a, b)
        small = min(a, b)
        while small > 0:
            tmp = small
            small = big % small
            big = tmp
        return big
