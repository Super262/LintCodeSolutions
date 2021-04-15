class Solution:
    """
    @param str: the string
    @return: the number of substrings
    """

    def stringCount(self, s: str) -> int:
        if not s:
            return 0
        answer = 0
        right = 1
        for left in range(len(s)):
            if s[left] != "0":
                continue
            right = max(right, left + 1)
            while right < len(s) and s[right] == "0":
                right += 1
            answer += right - left
        return answer
