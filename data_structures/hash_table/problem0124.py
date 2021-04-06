class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, nums: list) -> int:
        nums_pool = set(nums)
        max_len = 0
        for n in nums:
            # This is very important because we must find the start (minimal) of the expected sequence first!
            # Otherwise, the program will run with timeout!
            if n - 1 in nums_pool:
                continue

            next_n = n + 1
            while next_n in nums_pool:
                next_n += 1
            max_len = max(max_len, next_n - n)
        return max_len
