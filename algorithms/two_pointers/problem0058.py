class Solution:

    def fourSum(self, numbers: list, target: int) -> list:
        if not numbers or len(numbers) < 4:
            return []
        bound_d = len(numbers)
        bound_b = bound_d - 2
        bound_a = bound_b - 1
        numbers.sort()
        results = []
        for a in range(bound_a):
            if a > 0 and numbers[a - 1] == numbers[a]:
                continue
            for b in range(a + 1, bound_b):
                if b > a + 1 and numbers[b - 1] == numbers[b]:
                    continue
                prefix = [numbers[a], numbers[b]]
                self.two_sum(numbers, b + 1, bound_d - 1, target - numbers[a] - numbers[b], prefix, results)
        return results

    def two_sum(self, sorted_arr: list, start: int, end: int, target: int, prefix: list, results: list) -> None:
        while start < end:
            if sorted_arr[start] + sorted_arr[end] == target:
                temp = list(prefix)
                temp.append(sorted_arr[start])
                temp.append(sorted_arr[end])
                results.append(temp)
                end -= 1
                start += 1

                # Don't forget this part!
                while 0 < start < end and sorted_arr[start - 1] == sorted_arr[start]:
                    start += 1

            elif sorted_arr[start] + sorted_arr[end] > target:
                end -= 1
            else:
                start += 1
