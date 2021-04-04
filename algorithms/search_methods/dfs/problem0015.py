class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums: list) -> list:
        results = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], results)
        return results

    def dfs(self, nums: list, visited: list, permutation: list, results: list):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, results)
            permutation.pop()
            visited[i] = False
