class Solution:

    def kClosestNumbers(self, A: list, target: int, k: int) -> list:
        result = []
        if not A:
            return result
        right = self.find_closest_upper(A, target)
        left = right - 1
        for _ in range(k):
            if self.is_left_closer(A, left, target, right):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        return result

    def find_closest_upper(self, nums: list, target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        # 最后一定要返回数组长度作为无效值
        return len(nums)

    def is_left_closer(self, nums: list, left: int, target: int, right: int) -> bool:
        # 注意：nums[left]和nums[right]要和target相比较，而不是要和nums[mid]比较
        if left < 0:
            return False
        if right >= len(nums):
            return True
        dl = abs(target - nums[left])
        dr = abs(target - nums[right])
        if dl == dr:
            return nums[left] <= nums[right]
        else:
            return dl <= dr
