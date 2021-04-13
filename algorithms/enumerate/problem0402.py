class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, a: list) -> list:
        start = 0
        import sys
        max_sum = -sys.maxsize
        current_sum = -sys.maxsize
        result = [0, 0]
        for i in range(len(a)):
            if current_sum < 0:
                current_sum = a[i]
                start = i
            else:
                current_sum += a[i]
            end = i
            if current_sum > max_sum:
                result[0] = start
                result[1] = end
                max_sum = current_sum
        return result
