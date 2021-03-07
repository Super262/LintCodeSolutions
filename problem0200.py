class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome1(self, s):
        # Dynamic Programming
        if not s:
            return s
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True
        start, longest = 0, 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length > longest:
                    start = i
                    longest = length
        return s[start:start + longest]

    def longestPalindrome2(self, s):
        # Iteration from the center.
        if not s:
            return s
        answer = (1, 0)
        for mid in range(len(s)):
            answer = max(answer, self.get_longest_palindrome_from(s, mid, mid))
            answer = max(answer, self.get_longest_palindrome_from(s, mid, mid + 1))
        return s[answer[1]:answer[1] + answer[0]]

    def get_longest_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1
