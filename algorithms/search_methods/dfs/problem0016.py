class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        results = []
        visited = [False] * len(nums)
        self.dfs(sorted(nums), visited, [], results)
        return results

    def dfs(self, nums: list, visited: list, permutation: list, results: list):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]):
                continue
            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, results)
            permutation.pop()
            visited[i] = False
