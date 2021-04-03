class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums: list) -> list:
        results = []
        nums_copied = sorted(nums)
        self.helper(nums_copied, 0, [], results)
        return results

    def helper(self, nums: list, index: int, subset: list, results: list) -> None:
        results.append(list(subset))
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.helper(nums, i + 1, subset, results)
            subset.pop()
