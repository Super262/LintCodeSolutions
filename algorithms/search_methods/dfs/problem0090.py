class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, a: list, k: int, target: int) -> list:
        a_copied = list(a)
        a_copied.sort()
        results = []
        self.dfs(a_copied, [], results, 0, k, target)
        return results

    def dfs(self, a: list, combination: list, results: list, start_index: int, k: int, target) -> None:
        if len(combination) == k:
            if target == 0:
                results.append(list(combination))
            return
        for i in range(start_index, len(a)):
            if a[i] > target:
                return
            combination.append(a[i])
            self.dfs(a, combination, results, i + 1, k, target - a[i])
            combination.pop()
