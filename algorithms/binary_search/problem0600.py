class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    def minArea(self, image: list, x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        up = self.find_first(image, 0, x, True)
        down = self.find_last(image, x, len(image) - 1, True)
        left = self.find_first(image, 0, y, False)
        right = self.find_last(image, y, len(image[0]) - 1, False)
        return (down - up + 1) * (right - left + 1)

    def find_last(self, image: list, start: int, end: int, need_check_row: bool) -> int:
        while start + 1 < end:
            mid = start + (end - start) // 2
            if (need_check_row and self.check_row(image, mid)) or (not need_check_row and self.check_col(image, mid)):
                start = mid
            else:
                end = mid
        if (need_check_row and self.check_row(image, end)) or (not need_check_row and self.check_col(image, end)):
            return end
        return start

    def find_first(self, image: list, start: int, end: int, need_check_row: bool) -> int:
        while start + 1 < end:
            mid = start + (end - start) // 2
            if (need_check_row and self.check_row(image, mid)) or (not need_check_row and self.check_col(image, mid)):
                end = mid
            else:
                start = mid
        if (need_check_row and self.check_row(image, start)) or (not need_check_row and self.check_col(image, start)):
            return start
        return end

    def check_row(self, image: list, row: int) -> bool:
        for col in range(len(image[0])):
            if image[row][col] == '1':
                return True
        return False

    def check_col(self, image: list, col: int) -> bool:
        for row in range(len(image)):
            if image[row][col] == '1':
                return True
        return False
