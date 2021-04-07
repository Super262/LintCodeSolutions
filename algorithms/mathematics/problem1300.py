class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """

    def canWinBash(self, n: int) -> bool:
        # We can not use memorization search to solve this problem because of overflow
        # , but we can yse the method to find this trick!
        return n % 4 != 0
