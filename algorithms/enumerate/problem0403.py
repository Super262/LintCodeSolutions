class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    # 分两种情况讨论：
    # 最大数组仍然是中间的某一段
    # 最大数组是去掉了中间的一段之后剩下的部分

    def continuousSubarraySumII(self, a: list) -> list:
        max_sub_start, max_sub_end, max_sum = self.find_max_sub_array(a)
        min_sub_start, min_sub_end, min_sum = self.find_max_sub_array([-num for num in a])  # 使用相反数，巧妙的做法
        min_sum = -min_sum
        total = sum(a)
        if total - min_sum <= max_sum or min_sub_end - min_sub_start + 1 == len(a):
            return [max_sub_start, max_sub_end]
        return [min_sub_end + 1, min_sub_start - 1]

    def find_max_sub_array(self, a: list) -> tuple:
        import sys
        max_sum = -sys.maxsize
        current_sum = -sys.maxsize
        current_range = [0, 0]
        max_sub_range = [0, 0]
        for i in range(len(a)):
            if current_sum < 0:
                current_sum = 0
                current_range[0] = i
            current_sum += a[i]
            current_range[1] = i
            if current_sum > max_sum:
                max_sum = current_sum
                max_sub_range[0] = current_range[0]
                max_sub_range[1] = current_range[1]
        return max_sub_range[0], max_sub_range[1], max_sum
