class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums: list, k: int) -> list:
        nums_copied = list(nums)
        self.partition_by_kth(nums_copied, 0, len(nums_copied) - 1, k)
        result = nums_copied[0:k]
        result.sort(reverse=True)
        return result

    def partition_by_kth(self, nums: list, start: int, end: int, k: int) -> None:
        if start >= end:
            return
        pivot = nums[start + (end - start) // 2]
        i = start
        j = end
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if start + k - 1 <= j:
            self.partition_by_kth(nums, start, j, k)
            return
        if start + k - 1 >= i:
            self.partition_by_kth(nums, i, end, k - (i - start))
