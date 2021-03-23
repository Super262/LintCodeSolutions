class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n: int) -> int:
        if n < 3:
            return n - 1
        f0 = 0
        f1 = 1
        fn = f1 + f0
        for i in range(4, n + 1):
            f0 = f1
            f1 = fn
            fn = f1 + f0
        return fn
