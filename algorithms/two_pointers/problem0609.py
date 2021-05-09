class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums: list, target: int) -> int:
        result = 0
        nums.sort()  # 千万不要忘记排序！
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            else:
                result += end - start  # 这个区间内的所有数字均满足要求
                start += 1  # 千万不要忘记递增start！
        return result
