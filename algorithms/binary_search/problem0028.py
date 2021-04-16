class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix: list, target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            mid_num = self.get_in_matrix(matrix, mid)
            if mid_num == target:
                return True
            elif mid_num < target:
                start = mid
            else:
                end = mid
        if self.get_in_matrix(matrix, start) == target:
            return True
        if self.get_in_matrix(matrix, end) == target:
            return True
        return False

    def get_in_matrix(self, matrix: list, index: int) -> int:
        row = index // len(matrix[0])
        col = index % len(matrix[0])
        return matrix[row][col]
