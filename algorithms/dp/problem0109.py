class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle: list) -> int:
        memo = dict()
        return self.dp_get_minimal(triangle, 0, 0, memo)

    def dp_get_minimal(self, triangle: list, y: int, x: int, memo: dict) -> int:
        if y == len(triangle):
            return 0
        if (y, x) in memo:
            return memo[(y, x)]
        current_sum = triangle[y][x] + min(self.dp_get_minimal(triangle, y + 1, x, memo),
                                           self.dp_get_minimal(triangle, y + 1, x + 1, memo))
        memo[(y, x)] = current_sum
        return current_sum
