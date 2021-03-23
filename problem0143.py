class Solution:

    def sortColors2(self, colors: list, k: int) -> None:
        if not colors:
            return
        ptr = 0
        len_range = range(len(colors))
        for t in range(1, k + 1):
            for i in len_range:
                if colors[i] != t:
                    continue
                colors[ptr], colors[i] = colors[i], colors[ptr]
                ptr += 1
