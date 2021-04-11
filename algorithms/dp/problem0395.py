class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values: list) -> bool:
        n = len(values)
        f2 = 0
        f1 = values[n - 1] - f2
        for i in range(n - 2, -1, -1):
            f0 = max(values[i] - f1, values[i] + values[i + 1] - f2)
            f2 = f1
            f1 = f0
        return f1 >= 0
