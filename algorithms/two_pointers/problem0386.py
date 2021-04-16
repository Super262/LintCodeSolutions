class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        ch_freq = dict()
        current_unique_count = 0
        answer = 0
        left = 0
        right = 0
        while right < len(s):
            ch_freq[s[right]] = ch_freq.get(s[right], 0) + 1
            if ch_freq[s[right]] == 1:
                current_unique_count += 1
            right += 1
            while left < right and current_unique_count > k:
                ch_freq[s[left]] = ch_freq.get(s[left], 0) - 1
                if ch_freq.get(s[left]) == 0:
                    current_unique_count -= 1
                left += 1
            answer = max(right - left, answer)
        return answer
