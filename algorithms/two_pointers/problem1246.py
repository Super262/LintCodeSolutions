class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """

    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        answer = 0
        counter = dict()
        max_freq = 0
        right = 0
        for left in range(len(s)):
            right = max(right, left)
            while right < len(s) and right - left - max_freq <= k:
                counter[s[right]] = counter.get(s[right], 0) + 1
                max_freq = max(max_freq, counter[s[right]])
                right += 1
            if right - left - max_freq > k:
                answer = max(answer, right - left - 1)
            else:
                answer = max(answer, right - left)
            counter[s[left]] = counter.get(s[left], 0) - 1
            max_freq = max(counter.values())
        return answer
