class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    # 双指针解法，不如利用哈希表
    def twoSum(self, numbers: list, target: int) -> list:
        if not numbers:
            return [-1, -1]
        num_pairs = [(num, index) for index, num in enumerate(numbers)]
        num_pairs.sort()
        left = 0
        right = len(num_pairs) - 1
        while left < right:
            if num_pairs[left][0] + num_pairs[right][0] < target:
                left += 1
            elif num_pairs[left][0] + num_pairs[right][0] < target:
                right -= 1
            else:
                return sorted([num_pairs[left][1], num_pairs[right][1]])
        return [-1, -1]
