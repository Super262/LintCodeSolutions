class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        existed_chars = set()
        left = 0
        right = 0
        while right < len(s):
            while left <= right and s[right] in existed_chars:
                existed_chars.remove(s[left])
                left += 1
            existed_chars.add(s[right])
            if right - left + 1 > max_len:
                max_len = right - left + 1
            right += 1
        return max_len
