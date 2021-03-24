class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        ch_freq = [0] * 256
        unique_count = 0
        result = 0
        left = 0
        right = 0
        while right < len(s):
            ch_freq[ord(s[right])] += 1
            if ch_freq[ord(s[right])] == 1:
                unique_count += 1
            right += 1
            while left < right and unique_count > k:
                ch_freq[ord(s[left])] -= 1
                if ch_freq[ord(s[left])] == 0:
                    unique_count -= 1
                left += 1
            if right - left > result:
                result = right - left
        return result