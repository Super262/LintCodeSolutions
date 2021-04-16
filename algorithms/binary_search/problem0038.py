class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix: list, target: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix) - 1
        col = 0
        count = 0
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if target == matrix[row][col]:
                count += 1
                row -= 1
                col += 1
            elif target > matrix[row][col]:
                col += 1
            else:
                row -= 1
        return count
