class Solution:

    def isPalindrome(self, s: str, start: int, end: int) -> tuple:
        if not s:
            return 0, 0, True
        while s[start] == s[end] and start < end:
            start += 1
            end -= 1
        return start, end, start >= end

    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """

    def validPalindrome(self, s: str) -> bool:
        # 学习这种减少重复代码的思路
        start, end, isPa = self.isPalindrome(s, 0, len(s) - 1)
        if isPa:
            return True
        return self.isPalindrome(s, start, end - 1)[2] or self.isPalindrome(s, start + 1, end)[2]
