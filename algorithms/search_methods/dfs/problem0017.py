class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums: list) -> list:
        results = []
        nums_copy = sorted(nums)
        self.helper(nums_copy, 0, [], results)
        return results

    def helper(self, nums: list, index: int, subset: list, results: list) -> None:
        if index >= len(nums):
            results.append(list(subset))
            return
        subset.append(nums[index])
        self.helper(nums, index + 1, subset, results)
        subset.pop()
        self.helper(nums, index + 1, subset, results)
