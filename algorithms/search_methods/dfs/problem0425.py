class Solution:
    """
    @param digits: A digital string
    @return: all possible letter combinations
    """

    def letterCombinations(self, digits: str) -> list:
        results = []
        if not digits:
            return results
        keywords = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.dfs(keywords, digits, 0, [], results)
        return results

    def dfs(self, keywords: list, digits: str, digit_index: int, prefix: list, results: list) -> None:
        if digit_index == len(digits):
            results.append("".join(prefix))
            return
        word = keywords[int(digits[digit_index])]
        for ch in word:
            prefix.append(ch)
            self.dfs(keywords, digits, digit_index + 1, prefix, results)
            prefix.pop()
