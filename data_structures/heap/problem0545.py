class Solution:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        self.k = k
        self.min_h = []

    """
    @param: num: Number to be added
    @return: nothing
    """

    def add(self, num: int) -> None:
        import heapq
        heapq.heappush(self.min_h, num)
        while len(self.min_h) > self.k:
            heapq.heappop(self.min_h)

    """
    @return: Top k element
    """

    def topk(self) -> list:
        return sorted(self.min_h, reverse=True)
