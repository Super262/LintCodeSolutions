class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums: list) -> list:
        results = []
        nums_copied = sorted(nums)
        self.helper(nums_copied, 0, [], results)
        return results

    def helper(self, nums: list, start_index: int, subset: list, results: list) -> None:
        results.append(list(subset))
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.helper(nums, i + 1, subset, results)
            subset.pop()
