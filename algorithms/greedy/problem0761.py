class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """

    def minElements(self, arr: list) -> int:
        if not arr:
            return 0
        arr.sort(reverse=True)
        half_sum = sum(arr) // 2
        current_sum = 0
        count = 0
        for num in arr:
            current_sum += num
            count += 1
            if current_sum > half_sum:
                return count
        return count
