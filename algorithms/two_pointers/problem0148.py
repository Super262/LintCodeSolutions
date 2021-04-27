class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums: list) -> None:
        if not nums:
            return
        ptr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for j in range(len(nums)):
            if nums[j] == 1:
                nums[j], nums[ptr] = nums[ptr], nums[j]
                ptr += 1
