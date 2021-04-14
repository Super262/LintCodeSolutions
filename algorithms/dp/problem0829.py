class Solution:
    """
    @param pattern: a string,denote pattern string
    @param s: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.helper(pattern, 0, s, 0, dict(), set())

    def helper(self, pattern: str, p_start: int, s: str, s_start: int, ch_to_word: dict, used_words: set) -> bool:
        if pattern is None or p_start == len(pattern):
            return s_start == len(s)
        ch = pattern[p_start]
        if ch in ch_to_word:
            word = ch_to_word[ch]
            if s_start + len(word) > len(s) or s[s_start:s_start + len(word)] != word:
                return False
            return self.helper(pattern, p_start + 1, s, s_start + len(word), ch_to_word, used_words)
        for w_len in range(1, len(s) - s_start + 1):
            word = s[s_start:s_start + w_len]
            if word in used_words:
                continue
            ch_to_word[ch] = word
            used_words.add(word)
            if self.helper(pattern, p_start + 1, s, s_start + w_len, ch_to_word, used_words):
                return True
            ch_to_word.pop(ch)
            used_words.remove(word)
        return False
