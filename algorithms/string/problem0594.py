class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    # KMP

    def strStr2(self, source: str, target: str) -> int:
        if source is None or target is None:
            return -1
        if target == "":
            return 0
        next_map = self.build_next_map(target)
        s_ch_index = 0
        t_ch_index = 0
        while s_ch_index < len(source):
            if source[s_ch_index] == target[t_ch_index]:
                t_ch_index += 1
                s_ch_index += 1
            elif t_ch_index:
                t_ch_index = next_map[t_ch_index - 1]
            else:
                s_ch_index += 1
            if t_ch_index == len(target):
                return s_ch_index - t_ch_index
        return -1

    def build_next_map(self, target: str) -> list:
        next_map = [0] * len(target)
        now = 0
        x = 1
        while x < len(target):
            if target[x] == target[now]:
                now += 1
                next_map[x] = now
                x += 1
            elif now:
                now = next_map[now - 1]
            else:
                next_map[x] = 0
                x += 1
        return next_map
