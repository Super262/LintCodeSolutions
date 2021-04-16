class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages: list, k: int) -> int:
        # 二分结果集
        if not pages:
            return 0
        min_time_cost = max(pages)
        max_time_cost = sum(pages)
        while min_time_cost + 1 < max_time_cost:
            mid = min_time_cost + (max_time_cost - min_time_cost) // 2
            if self.get_num_of_copiers(pages, mid) <= k:
                max_time_cost = mid
            else:
                min_time_cost = mid
        if self.get_num_of_copiers(pages, min_time_cost) <= k:
            return min_time_cost
        return max_time_cost

    def get_num_of_copiers(self, pages: list, time_limit: int) -> int:
        import sys
        copiers_count = 0
        last_copied_pages = time_limit  # 设置初始值为time_limit巧妙之处
        for p in pages:
            if p > time_limit:
                return sys.maxsize
            if last_copied_pages + p > time_limit:
                last_copied_pages = 0
                copiers_count += 1
            last_copied_pages += p
        return copiers_count
