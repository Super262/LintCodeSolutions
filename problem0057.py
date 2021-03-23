class Solution:

    def threeSum(self, numbers: list) -> list:
        if not numbers:
            return []
        results = []
        sorted_arr = sorted(numbers)
        for i in range(len(sorted_arr)):

            # Don't forget this part!
            if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
                continue

            self.two_sum(sorted_arr, i + 1, len(sorted_arr) - 1, -sorted_arr[i], results)
        return results

    def two_sum(self, sorted_arr: list, left: int, right: int, target: int, results: list) -> None:
        while left < right:
            if sorted_arr[left] + sorted_arr[right] == target:
                results.append([-target, sorted_arr[left], sorted_arr[right]])
                right -= 1
                left += 1

                # Don't forget this part!
                while left < right < len(sorted_arr) - 1 and sorted_arr[right] == sorted_arr[right + 1]:
                    right -= 1

            elif sorted_arr[left] + sorted_arr[right] > target:
                right -= 1
            else:
                left += 1
