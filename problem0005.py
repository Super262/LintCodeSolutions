class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n: int, nums: list) -> int:
        if not nums or n < 1:
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, n)

    def quick_select(self, nums: list, start: int, end: int, k: int) -> int:
        if start >= end:
            return nums[start]
        pivot = nums[start + (end - start) // 2]
        i = start
        j = end
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
        if start + k - 1 <= j:
            return self.quick_select(nums, start, j, k)
        if start + k - 1 >= i:
            return self.quick_select(nums, i, end, k - (i - start))
        return nums[j + 1]
