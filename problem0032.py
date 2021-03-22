class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source: str, target: str) -> str:
        if not source or not target:
            return ""
        count_t = [0] * 256
        unique_t = 0
        for ch in target:
            count_t[ord(ch)] += 1
            if count_t[ord(ch)] == 1:
                unique_t += 1
        count_s = [0] * 256
        unique_s = 0
        left = 0
        right = 0
        ans_left = -1
        ans_right = -1
        while left < len(source):
            while right < len(source) and unique_s < unique_t:
                count_s[ord(source[right])] += 1
                if count_s[ord(source[right])] == count_t[ord(source[right])]:
                    unique_s += 1
                right += 1
            if unique_s == unique_t:
                if ans_left == -1 or right - left < ans_right - ans_left:
                    ans_left = left
                    ans_right = right
            count_s[ord(source[left])] -= 1
            if count_s[ord(source[left])] == count_t[ord(source[left])] - 1:
                unique_s -= 1
            left += 1
        return source[ans_left:ans_right]