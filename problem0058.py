class Solution:

    def fourSum(self, numbers: list, target: int) -> list:
        results = []
        if not numbers:
            return results
        bound_a = len(numbers) - 3
        if bound_a < 1:
            return results
        bound_b = len(numbers) - 2
        bound_d = len(numbers)
        numbers.sort()
        for a in range(bound_a):
            if a > 0 and numbers[a - 1] == numbers[a]:
                continue
            for b in range(a + 1, bound_b):
                if b > a + 1 and numbers[b - 1] == numbers[b]:
                    continue
                self.two_sum(numbers, b + 1, bound_d, target - numbers[a] - numbers[b], numbers[a], numbers[b],
                             results)
        return results

    def two_sum(self, sorted_arr: list, start: int, end: int, target: int, prefix1: int, prefix2: int,
                results: list) -> None:
        while start < end - 1:
            if sorted_arr[start] + sorted_arr[end - 1] == target:
                results.append([prefix1, prefix2, sorted_arr[start], sorted_arr[end - 1]])
                end -= 1
                start += 1

                # Don't forget this part!
                while 0 < start < end - 1 and sorted_arr[start - 1] == sorted_arr[start]:
                    start += 1

            elif sorted_arr[start] + sorted_arr[end - 1] > target:
                end -= 1
            else:
                start += 1
