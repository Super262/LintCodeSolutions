class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers: list, target: int) -> list:
        numbers_dict = dict()
        expected_set = set()
        for i in range(len(numbers)):
            if numbers[i] in numbers_dict:
                # For repeating elements, only remember the first one.
                continue
            numbers_dict[numbers[i]] = i
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in expected_set:
                return [numbers_dict[t], i]
            expected_set.add(numbers[i])
        return [-1, -1]
