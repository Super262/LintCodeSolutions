class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates: list, target: int) -> list:
        candidates_unique = list(set(candidates))
        candidates_unique.sort()
        results = []
        self.dfs(candidates_unique, 0, target, [], results)
        return results

    def dfs(self, candidates: list, start_index: int, target: int, combination: list, results: list) -> None:
        if target < 0:
            return
        if target == 0:
            results.append(list(combination))
            return
        for i in range(start_index, len(candidates)):
            if candidates[i] > target:
                return
            combination.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], combination, results)
            combination.pop()
