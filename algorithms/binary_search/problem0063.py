class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """

    def search(self, a: list, target: int) -> bool:
        if not a:
            return False
        start = 0
        end = len(a) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # 选择最后一个值nums[end]为"标杆"，以应对特殊情况：正常的排序数组
            if a[mid] == a[end]:
                end -= 1
            elif a[mid] > a[end]:
                if a[start] <= target <= a[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if a[mid] <= target <= a[end]:
                    start = mid
                else:
                    end = mid
        return a[start] == target or a[end] == target
