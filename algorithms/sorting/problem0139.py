class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums: list) -> list:
        prefix_sum = [[0, i] for i in range(len(nums) + 1)]  # [sum,i] => [前缀和，索引]
        for i in range(1, len(prefix_sum)):
            prefix_sum[i][0] = nums[i - 1] + prefix_sum[i - 1][0]
        prefix_sum.sort(key=lambda item: item[0])
        result = [prefix_sum[0][1], prefix_sum[1][1]]
        mis_distance = abs(prefix_sum[0][0] - prefix_sum[1][0])
        for i in range(1, len(prefix_sum)):
            if abs(prefix_sum[i][0] - prefix_sum[i - 1][0]) < mis_distance:
                mis_distance = abs(prefix_sum[i][0] - prefix_sum[i - 1][0])
                result[0] = prefix_sum[i - 1][1]
                result[1] = prefix_sum[i][1]
        result.sort()
        result[1] -= 1  # 开区间[start, end)转换为闭区间[start, end - 1]
        return result
