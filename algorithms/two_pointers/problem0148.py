class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums: list) -> None:
        if not nums:
            return
        left = 0
        right = len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                # 在这种情况下，index不变，因为右侧被交换过来的数可能是1或0
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1
