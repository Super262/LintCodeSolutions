class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    # KMP https://www.zhihu.com/question/21923021/answer/1032665486

    def strStr2(self, source: str, target: str) -> int:

        # target不存在时，返回-1
        if source is None or target is None:
            return -1

        # target为空时，返回0（参考Java的indexOf()和C的strstr()）
        if target == "":
            return 0
        next_map = self.build_next_map(target)
        s_ch_index = 0  # source当前待匹配的字符的索引
        t_ch_index = 0  # target当前待匹配的字符的索引
        while s_ch_index < len(source):

            # 匹配成功，两个指针均后移
            if source[s_ch_index] == target[t_ch_index]:
                t_ch_index += 1
                s_ch_index += 1

            # 匹配未成功且target待匹配的字符不为首字符
            elif t_ch_index:
                t_ch_index = next_map[t_ch_index - 1]

            # 匹配未成功且target待匹配的字符为首字符
            else:
                s_ch_index += 1
            if t_ch_index == len(target):
                # 返回首字符位置
                return s_ch_index - t_ch_index
        return -1

    def build_next_map(self, target: str) -> list:

        # next[0] = 0
        next_map = [0] * len(target)
        now = 0
        x = 1
        while x < len(target):

            # 匹配成功，两个指针均后移
            if target[x] == target[now]:
                now += 1
                next_map[x] = now
                x += 1

            # 匹配未成功且now对应的字符不为首字符
            elif now:
                now = next_map[now - 1]

            # 匹配未成功且now对应的字符为首字符
            else:
                next_map[x] = 0
                x += 1
        return next_map
