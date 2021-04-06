class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs: list) -> list:
        results = []
        word_groups = {}
        for s in strs:
            s_sorted = self.count_and_sort(s)
            current_group = word_groups.get(s_sorted, None)
            if not current_group:
                current_group = []
                word_groups[s_sorted] = current_group
            current_group.append(s)
        for key in word_groups:
            if len(word_groups[key]) < 2:
                continue
            results.extend(word_groups[key])
        return results

    def count_and_sort(self, s: str) -> str:
        if not s:
            return ""
        char_table = [0] * 26
        for ch in s:
            char_table[ord(ch) - ord("a")] += 1
        result = []
        for ch_ord in range(len(char_table)):
            for _ in range(char_table[ch_ord]):
                result.append(chr(ch_ord + ord("a")))
        return "".join(result)
