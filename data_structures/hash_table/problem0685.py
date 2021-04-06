class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums: list, terminating_number: int) -> int:
        terminating_number_existed = False
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == terminating_number:
                terminating_number_existed = True
                break
        if not terminating_number_existed:
            return -1
        for num in nums:
            if counter.get(num, 0) == 1:
                return num
        return -1
