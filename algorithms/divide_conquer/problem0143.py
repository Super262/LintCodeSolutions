class Solution:

    def sortColors2(self, colors: list, k: int) -> None:
        if not colors or k < 1 or k > len(colors):
            return
        self.sort_by_divide(colors, 0, len(colors) - 1, 1, k)

    def sort_by_divide(self, colors: list, start_index: int, end_index: int, first_color: int, last_color: int) -> None:
        if end_index == start_index or first_color == last_color:
            return
        mid_color = first_color + (last_color - first_color) // 2
        i = start_index
        j = end_index
        while i <= j:
            while i <= j and colors[i] <= mid_color:  # 这里使用小于等于号，因为计算color_mid时结果偏左
                i += 1
            while i <= j and colors[j] > mid_color:
                j -= 1
            if i <= j:
                colors[i], colors[j] = colors[j], colors[i]
                i += 1
                j -= 1
        self.sort_by_divide(colors, start_index, j, first_color, mid_color)
        self.sort_by_divide(colors, i, end_index, mid_color + 1, last_color)
