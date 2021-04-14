class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """

    # 暂时还没有学会空间为O(1)的解法
    def wiggleSort(self, nums: list) -> None:
        if not nums:
            return
        n = len(nums)
        # 选取中位数或者中位数左侧较小的元素相当于选取第(nums.length - 1) / 2 + 1个元素（从1开始计数）
        smaller_median = self.partition_by_smaller_median(nums, 0, n - 1, (n - 1) // 2 + 1)
        answer = [smaller_median] * n
        left = 1
        if n % 2 == 0:
            right = n - 2
        else:
            right = n - 1
        for num in nums:
            if num < smaller_median:
                answer[right] = num
                right -= 2
            elif num > smaller_median:
                answer[left] = num
                left += 2
        for i in range(n):
            nums[i] = answer[i]

    def partition_by_smaller_median(self, nums: list, start: int, end: int, k: int) -> int:
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
            return self.partition_by_smaller_median(nums, start, j, k)
        if start + k - 1 >= i:
            return self.partition_by_smaller_median(nums, i, end, k - (i - start))
        return nums[j + 1]
