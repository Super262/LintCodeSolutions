class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums: list) -> list:
        nums.sort()
        queue = [[]]
        index = 0
        while index < len(queue):
            base_set = queue[index]
            for num in nums:
                if base_set and base_set[-1] >= num:
                    continue
                tmp = list(base_set)
                tmp.append(num)
                queue.append(tmp)
            index += 1
        return queue
