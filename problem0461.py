class Solution:

    def kthSmallest(self, k: int, nums: list) -> int:
        if k < 1 or not nums:
            return -1
        return self.quick_select_smallest(nums, 0, len(nums) - 1, k)

    def quick_select_smallest(self, nums: list, start: int, end: int, k: int) -> int:
        if start >= end:
            return nums[start]
        pivot = nums[start + (end - start) // 2]
        i = start
        j = end
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if start + k - 1 <= j:
            return self.quick_select_smallest(nums, start, j, k)
        if start + k - 1 >= i:
            return self.quick_select_smallest(nums, i, end, k - (i - start))
        return nums[j + 1]
