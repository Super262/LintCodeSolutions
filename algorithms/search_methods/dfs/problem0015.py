class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums: list) -> list:
        results = []
        self.dfs(nums, set(), [], results)
        return results

    def dfs(self, nums: list, visited: set, permutation: list, results: list):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return
        for n in nums:
            if n in visited:
                continue
            visited.add(n)
            permutation.append(n)
            self.dfs(nums, visited, permutation, results)
            permutation.pop()
            visited.remove(n)
