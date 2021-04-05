class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, s: str) -> list:
        ch_array = list(s)
        ch_array.sort()
        results = []
        visited = [False] * len(ch_array)
        self.dfs(ch_array, visited, [], results)
        return results

    def dfs(self, s: list, visited: list, permutation: list, results: list) -> None:
        if len(s) == len(permutation):
            results.append("".join(permutation))
            return
        for i in range(len(s)):
            if visited[i]:
                continue
            if i > 0 and s[i - 1] == s[i] and not visited[i - 1]:
                continue
            visited[i] = True
            permutation.append(s[i])
            self.dfs(s, visited, permutation, results)
            permutation.pop()
            visited[i] = False
