class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n: int) -> bool:
        f0 = False
        f1 = False
        f2 = False
        if n > 0:
            f1 = True
        for i in range(2, n + 1):
            f2 = not f1 or not f0
            f0 = f1
            f1 = f2
            f2 = False
        return f1
