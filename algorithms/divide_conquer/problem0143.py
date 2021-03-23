class Solution:

    def sortColors2(self, colors: list, k: int) -> None:
        if not colors or k < 1 or k > len(colors):
            return
        self.sort_by_divide(colors, 0, len(colors) - 1, 1, k)

    def sort_by_divide(self, colors: list, index_start: int, index_end: int, color_first: int, color_last: int) -> None:
        if index_end == index_start or color_first == color_last:
            return
        color_mid = color_first + (color_last - color_first) // 2
        i = index_start
        j = index_end
        while i <= j:
            while i <= j and colors[i] <= color_mid:  # 这里使用小于等于号，因为计算color_mid时结果偏左
                i += 1
            while i <= j and colors[j] > color_mid:
                j -= 1
            if i <= j:
                colors[i], colors[j] = colors[j], colors[i]
                i += 1
                j -= 1
        self.sort_by_divide(colors, index_start, j, color_first, color_mid)
        self.sort_by_divide(colors, i, index_end, color_mid + 1, color_last)
