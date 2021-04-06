class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs: list) -> list:
        results = []
        word_groups = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in word_groups:
                word_groups[s_sorted] = []
            word_groups[s_sorted].append(s)
        for key in word_groups:
            if len(word_groups[key]) < 2:
                continue
            results.extend(word_groups[key])
        return results
