class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers: list, target: int) -> list:
        num_to_index = dict()
        result_pair = set()
        for i in range(len(numbers)):
            if numbers[i] in num_to_index:
                # For repeating elements, only remember the first one.
                continue
            num_to_index[numbers[i]] = i
        for j in range(len(numbers)):
            t = target - numbers[j]
            if t in result_pair:
                return [num_to_index[t], j]
            result_pair.add(numbers[j])
        return [-1, -1]
